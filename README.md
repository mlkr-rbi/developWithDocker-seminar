# Develop With Docker
# Table of Contents

1. [Develop With Docker](#develop-with-docker)
   - [Building a Docker Image](#building-a-docker-image)
     - [Introduction to Docker Image Building](#introduction-to-docker-image-building)
     - [Components of a Docker Image](#components-of-a-docker-image)
     - [Building a Simple Docker Image](#building-a-simple-docker-image)
     - [Docker Build Process](#docker-build-process)
     - [Advanced Docker Image Techniques](#advanced-docker-image-techniques)
   - [Running a Docker Image](#running-a-docker-image)
     - [Launching Docker Containers](#launching-docker-containers)
     - [Docker Run Command](#docker-run-command)
     - [Managing Docker Containers](#managing-docker-containers)
     - [Container Persistence and Data Management](#container-persistence-and-data-management)
   - [Docker Image and Singularity](#docker-image-and-singularity)
     - [Introduction to Singularity](#introduction-to-singularity)
     - [Docker Image Compatibility with Singularity](#docker-image-compatibility-with-singularity)
   - [Development in Remote Docker Containers](#development-in-remote-docker-containers)
     - [Remote Docker Development Environment Setup](#remote-docker-development-environment-setup)
     - [Collaborative Development with Remote Docker Containers](#collaborative-development-with-remote-docker-containers)
     - [Debugging and Troubleshooting in Remote Docker Environments](#debugging-and-troubleshooting-in-remote-docker-environments)
     - [Security Considerations for Remote Docker Development](#security-considerations-for-remote-docker-development)

# Develop With Docker

## Building a Docker Image

### Introduction to Docker Image Building
- Dockerfile to virtual machine.


![image](https://github.com/kmihak/developWithDocker/assets/64592696/ddd395cb-4a85-4717-b06d-f0621cfb23ee)
1. Docker Build Command: `docker build -t ime:naziv --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) .`
2. Docker run command: `docker run -it -rm ime:naziv /bin/bash`
3. Docker Images Command: `docker images`
4. Docker PS Command: `docker ps`
5. Root Management Command to Open Docker Container Bash: `docker exec -u 0 -g 0 -it rm container_id_or_name bash`


- Explanation of Docker images and their role in containerized environments.

### Components of a Docker Image
- Understanding the Dockerfile: syntax, commands, and best practices.
- Image layers and their significance in optimizing Docker image builds.

### Building a Simple Docker Image
- Step-by-step guide to creating a basic Dockerfile.
- Incorporating dependencies and application code into the Docker image.

### Docker Build Process
- Explanation of the `docker build` command and its options.
- Hands-on demonstration of building a Docker image from the Dockerfile.

### Advanced Docker Image Techniques
- Multi-stage builds for optimizing image size and build efficiency.
- Utilizing build arguments and environment variables for flexibility.
- Best practices for caching and layer optimization in Docker image builds.

## Running a Docker Image

### Launching Docker Containers
- Overview of running Docker containers from Docker images.
- Understanding container lifecycles and management.

### Docker Run Command
- Explanation of the `docker run` command and its various options.
- Configuring container networking, volumes, and environment variables during container runtime.

### Managing Docker Containers
- Monitoring running containers using Docker CLI commands.
- Interacting with containerized applications using Docker exec.

### Container Persistence and Data Management
- Understanding Docker volumes and persistent storage.
- Strategies for managing data in Docker containers for reliability and scalability.

## Docker Image and Singularity

### Introduction to Singularity
- Comparison between Docker and Singularity for containerization.
- Use cases for Singularity in scientific computing and HPC environments.

### Docker Image Compatibility with Singularity
- Exploring compatibility issues and solutions when using Docker images with Singularity.
- Converting Docker images to Singularity format.

## Development in Remote Docker Containers

### Remote Docker Development Environment Setup
- Overview of remote development workflows using Docker containers.
- Configuring Docker for remote access and development.

### Collaborative Development with Remote Docker Containers
- Using remote Docker containers for team collaboration and shared development environments.
- Best practices for managing code and dependencies in remote Docker setups.

### Debugging and Troubleshooting in Remote Docker Environments
- Strategies for debugging applications running in remote Docker containers.
- Troubleshooting common issues encountered during remote development.

### Security Considerations for Remote Docker Development
- Best practices for securing remote Docker environments.
- Implementing access controls and encryption for remote Docker connections.
