import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
    def __init__(self) -> None:
        self.client_id = "spotify client id"
        self.client_secret = "spotify client token"
        self.redirect_uri = "https://www.mysite.com"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                       client_secret=self.client_secret,
                                                       redirect_uri=self.redirect_uri,
                                                       scope="user-library-read"))
        
        # results = sp.current_user_saved_tracks()
        # for idx, item in enumerate(results['items']):
        #     track = item['track']
        #     print(idx, track['artists'][0]['name'], " - ", track['name'])
        
        result = sp.current_user()
        print(result)