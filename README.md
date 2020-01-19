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
  -e ACCOUNTS='AAAAA,BBBBB' \
  --name stellar-exporter \
  registry.gitlab.com/ix.ai/stellar-exporter:latest
```

## Supported variables

| **Variable**  | **Default**                    | **Mandatory** | **Description**                                                                                                        |
|:--------------|:------------------------------:|:-------------:|:-----------------------------------------------------------------------------------------------------------------------|
| `ACCOUNTS`    | -                              | **YES**       | comma separated list of the accounts monitor the balances                                                              |
| `HORIZON_URL` | `https://horizon.stellar.org/` | **NO**        | The URL of the horizon server. For the Test network you can use `https://horizon-testnet.stellar.org/`                 |
| `LOGLEVEL`    | `INFO`                         | **NO**        | [Logging Level](https://docs.python.org/3/library/logging.html#levels)                                                 |
| `GELF_HOST`   | -                              | **NO**        | if set, the exporter will also log to this [GELF](https://docs.graylog.org/en/3.0/pages/gelf.html) capable host on UDP |
| `GELF_PORT`   | `12201`                        | **NO**        | Ignored, if `GELF_HOST` is unset. The UDP port for GELF logging                                                        |
| `PORT`        | `9188`                         | **NO**        | The port for prometheus metrics                                                                                        |

## Tags and Arch

Starting with version v0.4.0, the images are multi-arch, with builds for amd64, arm64 and armv7.
* `vN.N.N` - for example v0.4.0
* `latest` - always pointing to the latest version
* `dev-branch` - the last build on a feature/development branch
* `dev-master` - the last build on the master branch

## Resources:
* GitLab: https://gitlab.com/ix.ai/stellar-exporter
* GitHub: https://github.com/ix-ai/stellar-exporter
* Docker Hub: https://hub.docker.com/r/ixdotai/stellar-exporter

See also [ix.ai/crypto-exporter](https://gitlab.com/ix.ai/crypto-exporter) for more usage examples, including Prometheus configuration
