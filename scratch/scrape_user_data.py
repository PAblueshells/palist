import sys
import spotipy
import spotipy.util as util
import pandas as pd

# scope = 'user-library-read'

verbose=False
scope = 'user-library-read user-follow-read user-read-recently-played user-top-read'

#username='sarahlc888' # FILL THIS OUT BEFORE RUNNING (was too lazy to do command line args) 

username='1dv9mtkf3fqh5gs2j1fufyzsp' #jeffrey

# make sure you're logged out of spotify before trying new users, otherwise you'll get the songs of whoever is still logged in



def tracks_to_df(tracks):
    # adapted from https://towardsdatascience.com/how-to-create-large-music-datasets-using-spotipy-40e7242cc6a6

    # initialize empty dataframe
    features_list = ["artist","album","track_name",  "track_id", "artist_genre","album_genre",
    "danceability","energy","key","loudness","mode", 
    "speechiness","acousticness","instrumentalness","liveness","valence","tempo", "duration_ms","time_signature"]
    tracks_df = pd.DataFrame(columns=features_list)
    

    # Loop through every track, extract features, append to the df    
    for track in tracks['items']:
        if 'track' in track.keys():
            track = track['track']
        tracks_features = {}
        # populate metadata
        tracks_features["artist"] = track["album"]["artists"][0]["name"]
        tracks_features["album"] = track["album"]["name"]
        tracks_features["track_name"] = track["name"]
        tracks_features["track_id"] = track["id"]
        
        artist = sp.artist(track["artists"][0]["external_urls"]["spotify"])
        tracks_features["artist_genre"] = ','.join(artist["genres"])

        album = sp.album(track["album"]["external_urls"]["spotify"])
        tracks_features["album_genre"] = ','.join(album["genres"])


        # populate audio features
        audio_features = sp.audio_features(tracks_features["track_id"])[0]
        for feature in features_list[6:]:
            tracks_features[feature] = audio_features[feature]
        
        # Concat the dfs
        track_df = pd.DataFrame(tracks_features, index = [0])
        tracks_df = pd.concat([tracks_df, track_df], ignore_index = True)
    print(tracks_df.columns)
    return tracks_df


if __name__=='__main__':
    print(f'processing user {username}')

    token = util.prompt_for_user_token(username, scope)

    print(token)

    if not token:
        print("Can't get token for", username)
        exit(0)




    sp = spotipy.Spotify(auth=token)

    if verbose:
        print(sp.current_user())



    # saved tracks
    saved_tracks = sp.current_user_saved_tracks(limit=50)
    feature_df = tracks_to_df(saved_tracks)
    feature_df.to_csv(f'../dummy_data/user_features/{username}.saved.csv', sep=',', index=False)

    # top tracks
    top_tracks = sp.current_user_top_tracks(limit=50)
    feature_df = tracks_to_df(top_tracks)
    feature_df.to_csv(f'../dummy_data/user_features/{username}.top.csv', sep=',', index=False)
