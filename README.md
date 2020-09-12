# palist

## Auth flow
- Front end prompts [user login](https://developer.spotify.com/documentation/web-api/quick-start/) w/ Spotify
- Pass user 'id' attribute to back end for data analysis
    - Auth scopes listed [here](https://developer.spotify.com/documentation/general/guides/scopes). We will likely use user-library-read, user-follow-read, user-read-recently-played, and user-top-read

During testing, back end can prompt user login with Spotipy as done in `scratch/test_auth.py`

## Get started with Docker for development
In `palist/docker`, run the following commands to access bash in a docker image with all Python dependencies in `requirements.txt` installed and with this repo mounted at `usr/src/app` :
```
docker build -t palist-app . 
docker run -it -p 8888:8888 -v [PATH/palist]:/usr/src/app palist-app /bin/bash
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root # (to run jupyter)
```
We Dockerize our app once it is further along ([a simple guide](https://runnable.com/docker/python/dockerize-your-python-application)).

## Starting the [Flask](https://flask.palletsprojects.com/en/1.1.x/) app
From the root directory of the project, run:
```
cd musicanalyzer
export FLASK_APP=musicanalyzer.py
python -m flask run
```
Finally, navigate to the local url where the app is being served (127.0.0.1:5000)

## Notes
- API credentials are [here](https://developer.spotify.com/dashboard/applications), connected to Sarah's spotify acct

## Backend/Data Analysis Tasks
- [x] Make Dockerfile (for 2/23)
- [x] Set up test auth workflow (for 2/23)
- [ ] Explore audio features (for 3/1)
    - [ ] Look at how to combine features for groups of tracks (while capturing variation of taste)
        - [ ] Similarity scores (like R^2) based on how well users correlate in the histogram of each of their audio feature --> NMDS plot
