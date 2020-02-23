import sys
import spotipy
import spotipy.util as util
import pandas as pd

# scope = 'user-library-read'

verbose=False
scope = 'user-library-read user-follow-read user-read-recently-played user-top-read'

username=''

if verbose:
    print('processing user = {}'.format(username))

token = util.prompt_for_user_token(username, scope)


if token:
    sp = spotipy.Spotify(auth=token)

    if verbose:
        print(sp.current_user())

    # saved tracks
    saved_tracks = sp.current_user_saved_tracks()
    if verbose:
        for item in saved_tracks['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
        print()

    # top tracks
    top_tracks = sp.current_user_top_tracks()
    if verbose:
        for track in top_tracks['items']:
            print(track['name'] + ' - ' + track['artists'][0]['name'])
    
        print()

    # get features for top tracks  
    top_track_uris = [ top_tracks['items'][i]['uri'] for i in range(len(top_tracks)) ]    
    audio_feats = sp.audio_features(top_track_uris)
    print((audio_feats[0].keys()))
    feature_df = pd.DataFrame(audio_feats)
    print(feature_df.head())

    feature_df.to_csv('test_features.csv', sep=',', index=False)

else:
    print("Can't get token for", username)