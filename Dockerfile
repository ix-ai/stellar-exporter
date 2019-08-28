FROM alpine:latest
LABEL maintainer="docker@ix.ai"

ARG PORT=9308
ARG LOGLEVEL=INFO

RUN apk --no-cache upgrade && \
    apk add --no-cache python3-dev gcc musl-dev && \
    pip3 install --no-cache-dir stellar-base mnemonic toml prometheus_client pygelf

ENV LOGLEVEL=${LOGLEVEL} PORT=${PORT}

COPY src/stellar-exporter.py /

EXPOSE ${PORT}

ENTRYPOINT ["python3", "/stellar-exporter.py"]
