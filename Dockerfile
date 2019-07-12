FROM hub.ix.ai/docker/alpine:latest
LABEL ai.ix.maintainer="docker@ix.ai"

ENV LOGLEVEL=INFO

RUN apk add --no-cache python3-dev \
    pip3 install stellar-base

COPY stellar-exporter.py /

EXPOSE 9308

ENTRYPOINT ["python3", "/stellar-exporter.py"]
