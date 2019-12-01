FROM alpine:latest
LABEL maintainer="docker@ix.ai"

WORKDIR /app

COPY src/ /app

RUN apk --no-cache upgrade && \
    apk add --no-cache python3-dev gcc musl-dev libffi-dev make && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apk del --no-cache --purge gcc musl-dev libffi-dev make

COPY src/stellar-exporter.py /

EXPOSE 9308

ENTRYPOINT ["python3", "/app/stellar-exporter.py"]
