# Use the official R image from Docker Hub
FROM r-base
# Find the local file platform for local image build:
# run in shell: docker inspect --format='{{.Os}}/{{.Architecture}}' <IMAGE_NAME>
# FROM --platform=linux/amd64 <IME>:<TAG>

# user arguments 1000 could be root user in linux based systems
ARG USER_ID=1
ARG GROUP_ID=1

# Set the working directory in the container
WORKDIR /workspace

# Linux dependencies
RUN apt-get update && \
  apt-get install -y build-essential sudo unzip bzip2 autoconf && \ 
  # apt-get install -y git wget && \
  # Below is necessary for pytorch and some other C++ demanding dependencies
  # apt-get install -y gcc g++ make && \
  # apt-get install -y pkg-config && \
  # apt-get install -y software-properties-common && \
  # apt-get install -y openjdk-11-jre-headless && \
  rm -rf /var/lib/apt/lists/*
  
# Copy the R script into the container
# COPY helloworld.R /workspace/

# Install required R packages
RUN R -e "install.packages('dplyr', repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('ggplot2', repos='http://cran.rstudio.com/')"

COPY . /workspace
RUN useradd user -u $USER_ID -g $GROUP_ID -m -s /bin/bash
RUN chown -R $USER_ID:$GROUP_ID /workspace 
# Run the R script
CMD ["Rscript", "helloworld.R"]
