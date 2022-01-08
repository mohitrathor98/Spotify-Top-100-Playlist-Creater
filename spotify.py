import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

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
                                                       scope="playlist-modify-private"))    
    def get_user_id(self):
        result = self.sp.current_user()
        return result['id']
    
    def create_list(self, song_list, date):
        uri_list = []
        print("\nCollecting URIs....")
        for song in song_list:
            try:
                result = self.sp.search(q=f"track: {song} year: {date.split('-')[0]}")
                uri_list.append(result['tracks']['items'][0]['uri'])
            except:
                pprint("Not able to find: "+ song)
        return uri_list
    
    def create_playlist(self, date):
        try:
            result = self.sp.user_playlist_create(
                                user = self.user_id, 
                                name = f"{date} Billboard 100", 
                                public = False, 
                                description = f"These are top 100 songs on {date} "+
                                                "according to Billboard."
                                )
            pprint(result)
        except:
            pprint("Not able to create playlist.")
