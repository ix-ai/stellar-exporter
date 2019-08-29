FROM alpine:latest
LABEL maintainer="docker@ix.ai"

ARG PORT=9308
ARG LOGLEVEL=INFO

WORKDIR /app

COPY src/ /app

RUN apk --no-cache upgrade && \
    apk add --no-cache python3-dev gcc musl-dev && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apk del --no-cache --purge gcc musl-dev

ENV LOGLEVEL=${LOGLEVEL} PORT=${PORT}

COPY src/stellar-exporter.py /

EXPOSE ${PORT}

ENTRYPOINT ["python3", "/app/stellar-exporter.py"]
