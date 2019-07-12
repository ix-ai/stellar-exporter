FROM hub.ix.ai/docker/alpine:latest
LABEL ai.ix.maintainer="docker@ix.ai"

ENV LOGLEVEL=INFO

RUN pip3 install stellar

COPY stellar-exporter.py /

EXPOSE 9308

ENTRYPOINT ["python3", "/stellar-exporter.py"]
