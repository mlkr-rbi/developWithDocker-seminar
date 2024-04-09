# Use the official Python image from Docker Hub
FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime
# Find the local file platform for local image build:
# docker inspect --format='{{.Os}}/{{.Architecture}}' <IMAGE_NAME>
# FROM --platform=linux/amd64 <IME>:<TAG>

ARG USER_ID=1
ARG GROUP_ID=1

# Set the working directory in the container
WORKDIR /workspace

# Linux dependencies
RUN apt-get update && \
  apt-get install -y build-essential sudo unzip bzip2 autoconf && \ 
  apt-get install -y git wget && \
  
  # Below is necessary for pytorch and some other C++ demanding dependencies
  # apt-get install -y gcc g++ make && \
  # apt-get install -y pkg-config && \
  # apt-get install -y software-properties-common && \
  # apt-get install -y openjdk-11-jre-headless && \
  rm -rf /var/lib/apt/lists/*
  
# Copy the Python script into the container
# COPY helloworld.py /workspace/
COPY . /workspace

# update and install packages in python
RUN pip install --upgrade pip && \
  pip install -r req.txt
RUN echo $(ls -a)

# Add a repository from github to your image
# RUN git clone --depth=1 https://github.com/allenai/s2orc-doc2json.git repoName/
# if repo has instalation
# CMD python repoName/setup.py develop

# Add your user to the environment helps with mounts and creating and saving files
RUN useradd user -u $USER_ID -g $GROUP_ID -m -s /bin/bash
RUN chown -R $USER_ID:$GROUP_ID /workspace 

# Run the Python script
CMD ["python", "helloworld.py"]
