from app import app

from flask import Flask, render_template, redirect, request, session, make_response, session, redirect
import spotipy
import spotipy.util as util
from app.credentz import *
import requests

app.secret_key = SSK

API_BASE = 'https://accounts.spotify.com'

# Make sure you add this to Redirect URIs in the setting of the application dashboard
REDIRECT_URI = "http://127.0.0.1:5000/api_callback"

SCOPE = 'user-library-read' # TODO: set proper scopes for our app (default access: only public playlists)

# Set this to True for testing but you probably want it set to False in production.
SHOW_DIALOG = True

# authorization-code-flow Step 1. Have your application request authorization;
# the user logs in and authorizes access
@app.route("/")
def verify():
    auth_url = f'{API_BASE}/authorize?client_id={CLI_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SCOPE}&show_dialog={SHOW_DIALOG}'
    print(auth_url)
    return redirect(auth_url)


# authorization-code-flow Step 2.
# Have your application request refresh and access tokens;
# Spotify returns access and refresh tokens
@app.route("/api_callback")
def api_callback():
    session.clear()
    code = request.args.get('code')

    auth_token_url = f"{API_BASE}/api/token"
    res = requests.post(auth_token_url, data={
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":"http://127.0.0.1:5000/api_callback",
        "client_id":CLI_ID,
        "client_secret":CLI_SEC
        })

    res_body = res.json()
    print(res.json())
    session["toke"] = res_body.get("access_token")

    return redirect("analyze-music")


# authorization-code-flow Step 3.
# Use the access token to access the Spotify Web API;
# Spotify returns requested data
#
# TODO: interface with the data analysis application at this point.
# Data analysis team can take the access token stored in session['toke'], request what they need, 
# and calculate + return the results
@app.route("/analyze-music")
def analyze_music():
    sp = spotipy.Spotify(auth=session['toke'])
    results = sp.current_user_saved_tracks(limit=50)

    tracks = ''
    for idx, item in enumerate(results['items']):
        track = item['track']
        tracks += str(idx) + ' ' + track['artists'][0]['name'] + " – " + ' ' + track['name'] + '<br />'

    return tracks

