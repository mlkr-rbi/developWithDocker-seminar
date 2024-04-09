Docker image for python and jupyter lab. Build the docker image using your host user and group (id -u) and (id -g)

docker build -t cuda:example --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) .

Run jupyter with your user and group and add some more groups to your user when opening jupyter lab. <group-name> is one of the default groups on your server.

docker run -it --rm --gpus all --user $(id -u):$(id -g) --group-add <group-name> --shm-size=8g -p 8888:8888 -v ~/homeWorkDirectory:/home/user/remoteWorkDirectory -w /home/user/remoteWorkDirectory cuda:example jupyter lab --no-browser --ip=0.0.0.0 --port=8888

Copy-paste link to browser and change the 127.0.0.1 to the server name e.g. abac.zel.lo.
