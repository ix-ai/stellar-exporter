# stellar-exporter

[![Pipeline Status](https://gitlab.com/ix.ai/stellar-exporter/badges/master/pipeline.svg)](https://gitlab.com/ix.ai/stellar-exporter/)
[![Docker Stars](https://img.shields.io/docker/stars/ixdotai/stellar-exporter.svg)](https://hub.docker.com/r/ixdotai/stellar-exporter/)
[![Docker Pulls](https://img.shields.io/docker/pulls/ixdotai/stellar-exporter.svg)](https://hub.docker.com/r/ixdotai/stellar-exporter/)
[![Gitlab Project](https://img.shields.io/badge/GitLab-Project-554488.svg)](https://gitlab.com/ix.ai/stellar-exporter/)

A [Prometheus](https://prometheus.io) exporter for [Stellar](https://www.stellar.org/) written in python

## Usage
```
docker run --rm -it -p 9308:9308 \
  -e LOGLEVEL=DEBUG \
  -e GELF_HOST=graylog \
  --name stellar-exporter \
  registry.gitlab.com/ix.ai/stellar-exporter:latest
```

## Supported variables
* `ACCOUNTS` (no default - **mandatory**) - comma separated list of the accounts monitor the balances
* `GELF_HOST` (no default) - if set, the exporter will also log to this [GELF](https://docs.graylog.org/en/3.0/pages/gelf.html) capable host on UDP
* `GELF_PORT` (defaults to `12201`) - the port to use for GELF logging
* `PORT` (defaults to `9308`) - the listen port for the exporter
* `LOGLEVEL` (defaults to `INFO`)

## Resources:
* GitLab: https://gitlab.com/ix.ai/stellar-exporter
* Docker Hub: https://hub.docker.com/r/ixdotai/stellar-exporter

See also [ix.ai/crypto-exporter](https://gitlab.com/ix.ai/crypto-exporter) for more usage examples, including Prometheus configuration
