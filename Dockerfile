FROM alpine:latest
LABEL maintainer="docker@ix.ai"

WORKDIR /app

COPY src/ /app

RUN apk --no-cache upgrade && \
    apk add --no-cache python3 py3-toml py3-numpy py3-prometheus-client py3-pynacl py3-urllib3 py3-yarl && \
    apk add --no-cache python3-dev gcc musl-dev libffi-dev make && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apk del --no-cache --purge python3-dev gcc musl-dev libffi-dev make

EXPOSE 9188

ENTRYPOINT ["python3", "/app/stellar-exporter.py"]
