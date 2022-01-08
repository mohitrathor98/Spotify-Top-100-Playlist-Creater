import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
    def __init__(self) -> None:
        self.client_id = "Spotify client id"
        self.client_secret = "Spotify client secret"
        self.redirect_uri = "https://www.mysite.com"
        try:
            self.sp = self.authenticate_user()
            self.user_id = self.get_user_id()
        except Exception as e:
            raise e
        
        
    def authenticate_user(self):
        return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                       client_secret=self.client_secret,
                                                       redirect_uri=self.redirect_uri,
                                                       scope="user-library-read"))    
    def get_user_id(self):
        result = self.sp.current_user()
        return result['id']
