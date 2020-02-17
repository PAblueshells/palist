# palist
## Docker for development
Open shell in a docker image with all Python dependencies in requirements.txt and this repo mounted in `usr/src/app` using:
```
docker build -t palist-app . 
docker run -it -v [PATH TO GIT REPO]:/usr/src/app palist-app /bin/bash
```
