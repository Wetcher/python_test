FROM python:3

RUN mkdir -p /.cache/pip && chown 1000:1000 /.cache/pip