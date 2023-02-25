# Introduction
RUN echo 'Creating DLTools Runing Enviornment...'

FROM debian:stable-slim

#
RUN pip install -r requirements.txt && \
    python setup.py build && \
    python setup.py install
