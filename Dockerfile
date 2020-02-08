FROM alpine:latest
LABEL maintainer="docker@ix.ai" \
      ai.ix.repository="ix.ai/stellar-exporter"

COPY stellar-exporter/requirements.txt /stellar-exporter/requirements.txt

RUN apk --no-cache upgrade && \
    apk add --no-cache python3 py3-toml py3-numpy py3-prometheus-client py3-pynacl py3-urllib3 py3-yarl && \
    apk add --no-cache python3-dev gcc musl-dev libffi-dev make && \
    pip3 install --no-cache-dir -r stellar-exporter/requirements.txt && \
    apk del --no-cache --purge python3-dev gcc musl-dev libffi-dev make

COPY stellar-exporter/ /stellar-exporter
COPY stellar-exporter.sh /usr/local/bin/stellar-exporter.sh

EXPOSE 9188

ENTRYPOINT ["/usr/local/bin/stellar-exporter.sh"]
