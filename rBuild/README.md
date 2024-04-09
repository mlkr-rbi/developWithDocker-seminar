Docker image for python and jupyter lab. Build the docker image using your host user and group (id -u) and (id -g)

docker build -t rbase:exmple --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) .

Run R script within the docker container. <group-name> is one of the default groups on your server.

If your R script is using additional data from your local folders mount them to the correc path `-v ~/home/Work/Directory:/home/user/workspace`
docker run -it --rm --user $(id -u):$(id -g) --group-add <group-name> --shm-size=8g -p 8888:8888 -v ~/homeWorkDirectory:/home/user/remoteWorkDirectory -w /home/user/workspace rbase:example Rscript helloworld.R