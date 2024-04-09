FROM python:3.8.18-slim-bullseye
# FROM --platform=linux/amd64 vsc-start-docker-s2ocr-py-4161eff9e9f4f737c0d37587746d58c49fffa27ff9c25136db0a55ea680c9b53-uid:latest
ARG USER_ID=1
ARG GROUP_ID=1

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /workspace

RUN apt-get update && \
  apt-get install -y build-essential sudo unzip bzip2 autoconf && \ 
  apt-get install -y git wget && \
  # apt-get install -y gcc g++ make && \
  # apt-get install -y pkg-config && \
  # apt-get install -y software-properties-common && \
  # apt-get install -y openjdk-11-jre-headless && \
  rm -rf /var/lib/apt/lists/*

COPY . /workspace

RUN pip install --upgrade pip && \
  pip install -r requirements.txt
RUN echo $(ls -a)
RUN git clone --depth=1 https://github.com/allenai/s2orc-doc2json.git ocr/

CMD python ocr/setup.py develop

RUN useradd vscode -u $USER_ID -g $GROUP_ID -m -s /bin/bash
RUN chown -R $USER_ID:$GROUP_ID /workspace 