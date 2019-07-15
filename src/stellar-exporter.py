#!/usr/bin/env python3
""" A Prometheus exporter for Stellar """
import logging
import time
import os
import sys
import pygelf
from stellar_base.address import Address
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY, GaugeMetricFamily

LOG = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=os.environ.get("LOGLEVEL", "INFO"),
    format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def configure_logging():
    """ Configures the logging """
    gelf_enabled: False

    if os.environ.get('GELF_HOST'):
        GELF = pygelf.GelfUdpHandler(
            host=os.environ.get('GELF_HOST'),
            port=int(os.environ.get('GELF_PORT', 12201)),
            debug=True,
            include_extra_fields=True
        )
        LOG.addHandler(GELF)
        gelf_enabled = True
    LOG.info('Initialized logging with GELF enabled: {}'.format(gelf_enabled))


class StellarCollector:
    """ The StellarCollector class """
    accounts = {}
    settings = {}

    def __init__(self):
        self.settings = {
            'accounts': os.environ.get("ACCOUNTS", '').split(','),
        }

    def get_accounts(self):
        """ Connects to the Stellar network and retrieves the account information """
        for account in self.settings['accounts']:
            a = Address(address=account, network='public')
            a.get()
            for balance in a.balances:
                if balance.get('asset_code'):
                    currency = balance.get('asset_code')
                elif balance.get('asset_type') == 'native':
                    currency = 'XLM'
                else:
                    currency = balance.get('asset_type')
                self.accounts.update({
                    '{}-{}'.format(account, currency): {
                        'account': account,
                        'currency': currency,
                        'balance': float(balance.get('balance'))
                    }
                })

        LOG.debug('Found the following accounts: {}'.format(self.accounts))

    def describe(self):
        """ Just a needed method, so that collect() isn't called at startup """
        return []

    def collect(self):
        """ The actual metrics collector """
        metrics = {
            'account_balance': GaugeMetricFamily(
                'account_balance',
                'Account Balance',
                labels=['source_currency', 'currency', 'account', 'type']
            ),
        }
        self.get_accounts()
        for a in self.accounts:
            metrics['account_balance'].add_metric(
                value=self.accounts[a]['balance'],
                labels=[
                    self.accounts[a]['currency'],
                    self.accounts[a]['currency'],
                    self.accounts[a]['account'],
                    'stellar',
                ]
            )
        for metric in metrics.values():
            yield metric


if __name__ == '__main__':
    configure_logging()
    PORT = int(os.environ.get('PORT', 9308))
    LOG.info("Starting on port {}".format(PORT))
    REGISTRY.register(StellarCollector())
    start_http_server(PORT)
    while True:
        time.sleep(1)
