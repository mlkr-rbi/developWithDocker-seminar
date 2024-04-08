# Develop With Docker
## Table of Contents
   - [Building a Docker Image](#building-a-docker-image)
     - [Introduction to Docker Image Building](#introduction-to-docker-image-building)
     - [Components of a Docker Image](#components-of-a-docker-image)
     - [Building a Simple Docker Image](#building-a-simple-docker-image)
     - [Run Docker Image](#run-docker-image)
   - [Docker Image and Singularity](#docker-image-and-singularity)
     - [Introduction to Singularity](#introduction-to-singularity)
     - [Docker Image Compatibility with Singularity](#docker-image-compatibility-with-singularity)
   - [Development in Remote Docker Containers](#development-in-remote-docker-containers)
     - [Remote Docker Development Environment Setup](#remote-docker-development-environment-setup)
     - [Collaborative Development with Remote Docker Containers](#collaborative-development-with-remote-docker-containers)
     - [Developing in Remote Docker Environments](#developing-in-remote-docker-environments)
     - [Security](#security)

## Install Docker (Locally)
Linux: https://docs.docker.com/engine/install/ubuntu/
Windows Docker Desktop: https://docs.docker.com/desktop/install/windows-install/
Windows WSL2: https://techcommunity.microsoft.com/t5/windows-11/how-to-install-the-linux-windows-subsystem-in-windows-11/m-p/2701207
   - Linux: https://docs.docker.com/engine/install/ubuntu/

Macintosh: https://docs.docker.com/desktop/install/mac-install/

Use existing installation on one of the servers: **bea, jane or abacus**, ask system admin 
for group permissions. For complete server names checkout the department wiki pages.

## Building a Docker Image

   ### Introduction to Docker Image Building
   - Dockerfile creates virtual machine
   - example minimal dockerfile in repo
   
   ![create virtual image](https://github.com/kmihak/developWithDocker/assets/64592696/b56cb97a-57bc-4c43-a4b6-1b90c556210a)

   ### Components of a Docker Image
   - Understanding the **Dockerfile** syntax and commands:
```
# FROM: Specifies the base image for the Dockerfile.
FROM <image>[:<tag>] [AS <name>]

# RUN: Executes commands in the Docker image. Makes image snapshot!
RUN <command>

# COPY: Copies files or directories from the host into the Docker image.
COPY <src> <dest>

# WORKDIR: Sets the working directory for subsequent instructions.
WORKDIR /path/to/directory

# CMD: Specifies the default command to run when the container starts.
CMD ["executable", "param1", "param2"]

# ENTRYPOINT: Specifies the command to run when the container starts, which cannot be overridden by CMD.
ENTRYPOINT ["executable", "param1", "param2"]

# ENV: Sets environment variables in the Docker image.
ENV <key> <value>

...
```
   - Image layers and their significance in optimizing Docker image builds.
   
   1. Docker Build Command: `docker build -t <ime>:<naziv> --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) .`
   2. Docker run command: `docker run -it --rm <ime>:<naziv> /bin/bash`
   3. Docker Images Command: `docker images`
   4. Docker PS Command: `docker ps`
   5. Root Management Command to Open Docker Container Bash: `docker exec -u 0 -g 0 -it rm <container_id_or_name> bash`
   6. Download image to docker: `pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime`
   
![docker images](https://github.com/kmihak/developWithDocker/assets/64592696/af0b85ee-e6ff-4cfa-934b-0e861feb91f6)
Show docker images from **build** command using: `docker images`.

![Show docker ps](https://github.com/kmihak/developWithDocker/assets/64592696/7bc454d4-0858-48e5-9c9b-18aa4e27b2dc)
Shows docker containers from **run** command using `docker ps`.

   - Some more basic operations with images & containers:
   1. **Delete Image Command:**
      - Removes a Docker image forcefully: `docker image rm -f <f8fcad3b680c>`
      - Resumes execution of a stopped Docker container: `docker start <container-name/ID>`
      - Stop docker container `docker stop <container-name/ID>`
   
   2. **Tagging Image with Custom Repository and Tag:**
      - Description: Tags an existing Docker image with a custom repository name and tag.
      ```
      docker image tag server:latest <myname/name>:<otherName>
      docker image tag d583c3ac45fd <myname/name>:<otherName>
      ```

   ### Building a Simple Docker Image
   - Step-by-step guide to creating a basic docker image.
      - Step1: create directory: <your_pat/start-vm-project/>
      - Step2: copy dockerfile, requirements.txt, scriptToRun.py to directory.
      - Step3: Build the image and `docker build -t <ime>:<naziv> --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) .`

   ### Run Docker Image
   - Step3: **Do i need?**
      - a) virtual mounts: Yes: `-v ~/home/directory:/remoteHome/workingDirectory`,
      - b) gpus to use for computing `--gpus all` vs `--gpus '"device=0,2"'`,
      - c) what is my working directory `-w <home/user/set/working/dir/in/container`,
      - d) shared memory directory is limited to 64MB, but we increase this size since my application depend on this shared memory to 8GB `--shm-size=8g`,
      - e) port forwarding between container and "host machine" `-p 8888:8888`,
      - f) ...
   - Step4: JupyterLab in browser: 
   ```
docker run -it --rm --gpus all --user $(id -u):$(id -g) --group-add users --shm-size=8g -p 8888:8888 -v ~/homeWorkDirectory:/home/user/remoteWorkDirectory -w /home/user/remoteWorkDirectory <ime>:<tag> jupyter lab --no-browser --ip=0.0.0.0 --port=8888
```
   click on jupyter link to open jupyter lab and develop.
   - Step4': Run some script that needs all these flags:
```
docker run -it --rm --gpus all --user $(id -u):$(id -g) --group-add users --shm-size=8g -p 8888:8888 -v ~/homeWorkDirectory:/home/user/remoteWorkDirectory -w /home/user/remoteWorkDirectory <ime>:<tag> python <some_python_based_flags> my_script.py
```

## Docker Image and Singularity
Save your docker development image to file: ` docker save -o pathToFile/py-min.tar fe35d0fd6c24`

Sync image to the server with singularity: `rsync -avP path/to_directory/py-min.tar <username>@<server.hr>:/home/user/path/to_directory/`

Use gzip: `gzip py_min.tar`,  `rsync -avP path/to_directory/py-min.tar.gz mkeber@orthus.cir.irb.hr:/home/user/path/to_directory/`

   ![Docker to singularity container (1)](https://github.com/kmihak/developWithDocker/assets/64592696/c1a04438-cdf2-4243-a39e-0f69554d6be6)


   1. Build the Singularity Container from existing docker image: `singularity build <singularity_container.simg> docker-archive://<py-min.tar>`
   - Replace <py-min.tar> with the desired name for your docker image file. This command does not require sudo to create .simg singularity image.
   2. Create a Singularity Definition File (e.g., `singularityfile.def`):
   ```
   Bootstrap: docker
   From: name:tag
   
   %post
       # Execute your script inside the container
       python your_script.py
   ```
   Using singularityfile.def requires singularity grou priveleges. Pull the image from docker hub repositories
   
   3. Run the Singularity Container: `singularity exec --nv <singularity_container.simg> python helloworld.py`
   Replace "path/to/your_container.simg" with the path to your Singularity container file and your_script.py with the name of your Python script. `--nv` flag gives premissions to cuda.

`singularity exec --nv your_container.simg python -c your_script.py`

## Development in Remote Docker Containers (TBD)

### Remote Docker Development Environment Setup
- SSH keys

### Collaborative Development with Remote Docker Containers
- VSCODE ssha remote containers packages

### Developing in Remote Docker Environments
- VSCODE in remote container

### Security
