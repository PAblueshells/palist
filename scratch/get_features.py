import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

'''
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
'''
'''
for playlist in playlists['items']:
    tracks = sp.playlist_tracks(playlist['id'])
    for track in tracks['items']:
        track = track['track']
        #print(track['name'])
        audio_features = sp.audio_features(tracks=[track['uri']])
        
       # import pdb
       # pdb.set_trace()
        print(track['name'] + ' liveliness: {}'.format(audio_features[0]['energy']))
'''

user = sp.user('dbt556ctk5xwblkyeoll80wb6')
print(sp.current_user_top_artists())
#print(user)
