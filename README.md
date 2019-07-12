# stellar-exporter

A [Prometheus](https://prometheus.io) exporter for [Stellar](https://www.stellar.org/) written in python

## Usage
```
docker run --rm -it -p 9308:9308 \
  -e LOGLEVEL=DEBUG \
  --name stellar-exporter \
  hub.ix.ai/docker/stellar-exporter:latest
```

## Supported variables
* `ACCOUNTS` (no default) - comma separated list of the accounts monitor the balances
* `LOGLEVEL` (defaults to `INFO`)
