FROM registry.gitlab.com/ix.ai/alpine:latest
LABEL MAINTAINER="docker@ix.ai"

ARG PORT=9308

RUN apk add --no-cache python3-dev &&\
    pip3 install --no-cache-dir stellar-base mnemonic toml

ENV LOGLEVEL=INFO PORT=${PORT}

COPY src/stellar-exporter.py /

EXPOSE ${PORT}

ENTRYPOINT ["python3", "/stellar-exporter.py"]
