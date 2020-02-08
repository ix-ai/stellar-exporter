#!/usr/bin/env python3
""" A Prometheus exporter for Stellar """
import logging
import time
import os
from stellar_sdk.server import Server
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY, GaugeMetricFamily
from .lib import constants

log = logging.getLogger(__package__)
version = f'{constants.VERSION}-{constants.BUILD}'


class StellarCollector:
    """ The StellarCollector class """
    accounts = {}
    settings = {}

    def __init__(self, **kwargs):
        self.settings = {
            'accounts': [],
            'server': Server(horizon_url=kwargs['horizon_url']),
        }
        if kwargs.get('accounts'):
            self.settings['accounts'] = kwargs['accounts'].split(',')

    def get_accounts(self):
        """ Connects to the Stellar network and retrieves the account information """
        log.info('Retrieving accounts')
        for account in self.settings['accounts']:
            balances = self.settings['server'].accounts().account_id(account).call().get('balances')
            if isinstance(balances, list):
                for balance in balances:
                    if balance.get('asset_code'):
                        currency = balance.get('asset_code')
                    elif balance.get('asset_type') == 'native':
                        currency = 'XLM'
                    else:
                        currency = balance.get('asset_type')
                    self.accounts.update({
                        f'{account}-{currency}': {
                            'account': account,
                            'currency': currency,
                            'balance': float(balance.get('balance'))
                        }
                    })

        log.debug(f'Found the following accounts: {self.accounts}')

    def describe(self):
        """ Just a needed method, so that collect() isn't called at startup """
        return []

    def collect(self):
        """ The actual metrics collector """
        metrics = {
            'account_balance': GaugeMetricFamily(
                'account_balance',
                'Account Balance',
                labels=['currency', 'account', 'type']
            ),
        }
        self.get_accounts()
        for a in self.accounts:
            metrics['account_balance'].add_metric(
                value=self.accounts[a]['balance'],
                labels=[
                    self.accounts[a]['currency'],
                    self.accounts[a]['account'],
                    'stellar',
                ]
            )
        for metric in metrics.values():
            yield metric


def _test(collector):
    for metric in collector.collect():
        log.info(f"{metric}")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 9188))
    settings = {
        'horizon_url': os.environ.get('HORIZON_URL', 'https://horizon.stellar.org/'),
        'accounts': os.environ.get("ACCOUNTS", []),
    }
    log.warning(f"Starting {__package__} {version} on port {port}")

    if os.environ.get('TEST', False):
        _test(StellarCollector(
            horizon_url='https://horizon.stellar.org/',
            accounts='GA5XIGA5C7QTPTWXQHY6MCJRMTRZDOSHR6EFIBNDQTCQHG262N4GGKTM'  # kraken
            ',GD6RMKTCHQGEOGYWIKSY5G7QWXPZOAEZIKPKEVZUAXOQCZRVBRRFGLJM'  # NydroEnergy
            ',GCNSGHUCG5VMGLT5RIYYZSO7VQULQKAJ62QA33DBC5PPBSO57LFWVV6P'  # InterstellarExchange
            ))
    else:
        REGISTRY.register(StellarCollector(**settings))
        start_http_server(port)
        while True:
            time.sleep(1)
