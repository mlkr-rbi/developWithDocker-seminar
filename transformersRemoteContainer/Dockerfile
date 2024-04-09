FROM nvidia/cuda:12.1.0-cudnn8-devel-ubuntu20.04
## FROM --platform=linux/amd64 vsc-start-docker-s2ocr-py-4161eff9e9f4f737c0d37587746d58c49fffa27ff9c25136db0a55ea680c9b53-uid:latest
# SRCE WORKING EXAMPLE CUDA 11.3: FROM nvidia/cuda:11.3.1-devel-ubuntu20.04
LABEL maintainer="Hugging Face"

ARG DEBIAN_FRONTEND=noninteractive
ARG USER_ID=1
ARG GROUP_ID=1

RUN apt update
RUN apt install -y git libsndfile1-dev tesseract-ocr espeak-ng python3 python3-pip ffmpeg
RUN python3 -m pip install --no-cache-dir --upgrade pip

ARG REF=main
RUN git clone https://github.com/huggingface/transformers && cd transformers && git checkout $REF

# If set to nothing, will install the latest version
ARG PYTORCH='2.1.0'
ARG TORCH_VISION=''
ARG TORCH_AUDIO=''
# Example: `cu102`, `cu113`, etc. srce 'cu113'
ARG CUDA='cu121'

RUN [ ${#PYTORCH} -gt 0 ] && VERSION='torch=='$PYTORCH'.*' ||  VERSION='torch'; python3 -m pip install --no-cache-dir -U $VERSION --extra-index-url https://download.pytorch.org/whl/$CUDA
RUN [ ${#TORCH_VISION} -gt 0 ] && VERSION='torchvision=='TORCH_VISION'.*' ||  VERSION='torchvision'; python3 -m pip install --no-cache-dir -U $VERSION --extra-index-url https://download.pytorch.org/whl/$CUDA
RUN [ ${#TORCH_AUDIO} -gt 0 ] && VERSION='torchaudio=='TORCH_AUDIO'.*' ||  VERSION='torchaudio'; python3 -m pip install --no-cache-dir -U $VERSION --extra-index-url https://download.pytorch.org/whl/$CUDA

RUN python3 -m pip install --no-cache-dir -e ./transformers[dev-torch,testing,video]

RUN python3 -m pip uninstall -y tensorflow flax

RUN python3 -m pip install --no-cache-dir git+https://github.com/facebookresearch/detectron2.git pytesseract
RUN python3 -m pip install -U "itsdangerous<2.1.0"

# When installing in editable mode, `transformers` is not recognized as a package.
# this line must be added in order for python to be aware of transformers.
RUN cd transformers && python3 setup.py develop
WORKDIR /workspace
COPY requirements.txt /workspace
RUN python3 -m pip install -r requirements.txt

RUN mkdir /workspace/data

RUN useradd user -u $USER_ID -g $GROUP_ID -m -s /bin/bash
RUN chown -R $USER_ID:$GROUP_ID /workspace 