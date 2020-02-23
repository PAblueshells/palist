import sys
import spotipy
import spotipy.util as util

# scope = 'user-library-read'


scope = 'user-library-read user-follow-read user-read-recently-played user-top-read'


# username = 'placeholder'
username=''
print('processing {}'.format(username))
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)

    print(sp.current_user())
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])

else:
    print("Can't get token for", username)