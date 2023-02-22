# Crone.ar Backend

This project was bootstrapped with [Flask](https://flask.palletsprojects.com/en/2.1.x/)

## Pre-requisites

In order to run this project, you must have these dependences installed on your OS:

  * Poetry
  * Docker
  * Docker Compose

## Pre-requisites installation
#### NOTE: This guide is intended for Linux environments

### Install Poetry

```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

###  Resolves the dependencies, and installs them

```sh
poetry install
```

### Export requirements.txt file

```sh
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

## Running the project locally

In VSC right click on main.py and press Run Python File in Terminal

### Install Docker ( for Windows follow  [this guide.](https://docs.docker.com/desktop/windows/install/))

```sh
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable docker --now
docker
```

- You can now get started with using docker, with sudo. If you want to add yourself to the docker group to use docker without sudo, an additional step is needed:

```sh
sudo usermod -aG docker $USER 
newgrp docker
docker run hello-world
```

### Install Docker Compose

```sh
 sudo apt install docker-compose
```

## Running the project locally

### Instructions to Docker to cease the container and execute it

```sh
docker-compose up
```

- It can also activate detachment mod, and run the containers in the background

```sh
docker-compose up -d
```

###  Allows you to see the containers running
  
```sh 
docker-compose ps
```

###  Turn off all the services he raised with Docker-Compos Up
  
```sh 
docker-compose stop
```

#### To list the images that your Docker host has locally, run the command below:

```sh
docker image ls
```

#### Removing image

Delete the docker image with the docker image id mentioned in the command:

```sh
docker rm <ID>
```

#### List dangling images

Docker images consist of multiple layers. Dangling images are layers that have no relationship to any tagged images. They no longer serve a purpose and consume disk space

```sh
docker images -f dangling=true
```

#### Remove dangling images

Delete the docker dangling image with the docker image id mentioned in the command:

```sh
docker image prune
```

#### Upload image to docker

```sh
docker login
docker tag <imageId or imageName> <hostname>:<repository-port>/<image>:<tag>
docker tag """""""""" wolf2214/cronear
docker push wolf2214/cronear:latest
```

### Flask Documentation

#### Form URLs in our code



## Learn More

To learn Poetry, check out the [Poetry documentation](https://python-poetry.org/docs/).
To learn Docker, check out the [Docker documentation](https://docs.docker.com/).
# ¡Happy coding!
