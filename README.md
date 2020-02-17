# palist
## Get started with Docker for development
In `./docker`, run the following commands to access bash in a docker image with all Python dependencies in `requirements.txt` installed and with this repo mounted at `usr/src/app` :
```
docker build -t palist-app . 
docker run -it -v [PATH TO GIT REPO]:/usr/src/app palist-app /bin/bash
```
We Dockerize our app once it is further along ([a simple guide](https://runnable.com/docker/python/dockerize-your-python-application)).
