# Develop With Docker
# Table of Contents
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

## Building a Docker Image

   ### Introduction to Docker Image Building
   - Dockerfile creates virtual machine
   - example minimal dockerfile in repo
   
   ![create virtual image](https://github.com/kmihak/developWithDocker/assets/64592696/9e8d4fe0-e47a-41df-a4cf-d617c3a89a68)

   ### Components of a Docker Image
   - Understanding the Dockerfile syntax and commands:
```
FROM <image>[:<tag>] [AS <name>]
RUN <command>
COPY <src> <dest>
WORKDIR /path/to/directory
CMD ["executable", "param1", "param2"]               # CMD: Specifies the default command to run when the container starts.
ENTRYPOINT ["executable", "param1", "param2"]
ENV <key> <value>
```
   - Image layers and their significance in optimizing Docker image builds.
   
   1. Docker Build Command: `docker build -t ime:naziv --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) .`
   2. Docker run command: `docker run -it --rm ime:naziv /bin/bash`
   3. Docker Images Command: `docker images`
   4. Docker PS Command: `docker ps`
   5. Root Management Command to Open Docker Container Bash: `docker exec -u 0 -g 0 -it rm container_id_or_name bash`
   6. Download image to docker: `docker pull pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime`
   
   
   - Some more basic operations with images & containers:
   1. **Delete Image Command:**
      - Description: Removes a Docker image forcefully: ` docker image rm -f 229ffe904fb8`
      - Resumes execution of a stopped Docker container: `docker start <container-name/ID>`
      - Stop docker container `docker stop <container-name/ID>`
   
   2. **Tagging Image with Custom Repository and Tag:**
      - Description: Tags an existing Docker image with a custom repository name and tag.
      ```
      docker image tag server:latest myname/name:otherName
      docker image tag d583c3ac45fd myname/name:otherName
      ```

   ### Building a Simple Docker Image
   - Step-by-step guide to creating a basic Dockerfile.
   
   - Step1: create directory: start-vm-project
   - Step2: dockerfile, requirements.txt, scriptToRun.py
   `docker build -t ime:naziv --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) .`

   ### Run Docker Image
   
   - Step3: Do i need virtual mounts: Yes: -v ~/home/directory:/remoteHome/workingDirectory
   - Step4: JupyterLab: 
   `docker run -it --rm --gpus all --user $(id -u):$(id -g) --group-add users --shm-size=8g -p 8889:8889 -v ~/homeWorkDirectory:/home/user/remoteWorkDirectory -w /home/user/remoteWorkDirectory ime:tag jupyter lab --no-browser --ip=0.0.0.0 --port=8889`
   click on jupyter link to open jupyter lab
   - Step5: develop

## Docker Image and Singularity
   ![Docker to singularity container](https://github.com/kmihak/developWithDocker/assets/64592696/069834fa-eccb-44b6-ab37-16baee93a847)
   
   
   1. Create a Singularity Definition File (e.g., singularityDefinition.def):
   ```
   Bootstrap: docker
   From: name:tag
   
   %post
       # Execute your script inside the container
       python your_script.py
   ```
   2. Build the Singularity Container: `singularity build your_container.simg singularity_definition.def`
   - Replace your_container.simg with the desired name for your Singularity container file.
   3. Run the Singularity Container: `singularity exec "path/to/your_container.simg" python your_script.py`
   Replace "path/to/your_container.simg" with the path to your Singularity container file and your_script.py with the name of your Python script.

## Development in Remote Docker Containers (TBD)

### Remote Docker Development Environment Setup
- SSH keys

### Collaborative Development with Remote Docker Containers
- VSCODE ssha remote containers packages

### Developing in Remote Docker Environments
- VSCODE in remote container

### Security
