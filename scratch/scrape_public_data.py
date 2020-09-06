import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd 

def analyze_playlist(creator, playlist_id):
    
    # Create empty dataframe
    playlist_features_list = ["artist","album","track_name",  "track_id","danceability","energy","key","loudness","mode", "speechiness","instrumentalness","liveness","valence","tempo", "duration_ms","time_signature"]
    
    playlist_df = pd.DataFrame(columns = playlist_features_list)
    
    # Loop through every track in the playlist, extract features and append the features to the playlist df
    
    playlist = sp.user_playlist_tracks(creator, playlist_id)["items"]
    for track in playlist:
        # Create empty dict
        playlist_features = {}
        # Get metadata
        try:
            playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        except IndexError:
            if len(track["track"]["album"]["artists"])==0:
                playlist_features["artist"] = None
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]
        
        if playlist_features["track_id"]==None:
            print(f'skipping {playlist_features["track_name"]}, missing track id')
            continue # skip in case of missing track id

        # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]

        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]
        
        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)
        
    return playlist_df


token = SpotifyClientCredentials()
cache_token = token.get_access_token()
sp = spotipy.Spotify(cache_token)



user = "spotify"
pl_id = "37i9dQZF1DWYJ5kmTbkZiz" # note: access original playlist info using pl_id: https://open.spotify.com/playlist/37i9dQZF1DWYJ5kmTbkZiz
analyze_playlist(user, pl_id).to_csv(f'../dummy_data/track_features/{user}.topTracks2010s.csv', sep=',', index=False)


analyze_playlist("12160726861", "6yPiKpy7evrwvZodByKvM9").to_csv(f'../dummy_data/track_features/oscar.longestPlaylistEver.csv', sep=',', index=False)
