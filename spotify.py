
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
        
        self.playlist_id = None
        
        
    def authenticate_user(self):
        
        return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                       client_secret=self.client_secret,
                                                       redirect_uri=self.redirect_uri,
                                                       scope="playlist-modify-public"))
            
    def get_user_id(self):
        
        result = self.sp.current_user()
        return result['id']
    
    
    def create_list(self, song_list, date):
        
        uri_list = []
        pprint("Collecting URIs....")
        for song in song_list:
            try:
                result = self.sp.search(q=f"track: {song} year: {date.split('-')[0]}")
                uri_list.append(result['tracks']['items'][0]['uri'])
            except:
                pprint("Not able to find: "+ song.strip())
            
        pprint("Done collevting URIs")
        return uri_list
    
    
    def create_playlist(self, date):
        
        playlist_name = f"{date} Billboard 100"
        try:
            result = self.sp.user_playlists(self.user_id)
            for list in result['items']:
                if list['name'] == playlist_name:
                    pprint("Playlist already exists")
                    self.playlist_id = list['id']
                    return
                
            result = self.sp.user_playlist_create(
                                user = self.user_id, 
                                name = playlist_name, 
                                public = True, 
                                description = f"These are top 100 songs on {date} "+
                                                "according to Billboard."
                                )
            self.playlist_id = result['id']
            pprint("Playlist created: " + playlist_name)
            
        except:
            pprint("Not able to create playlist.")
            
    
    def get_current_song_in_playlist(self):
        
        try:
            
            result = self.sp.playlist_tracks(self.playlist_id)
            if len(result['items']) > 0:
                return [songs['track']['uri'] for songs in result['items']]
            else:
                return []
        
        except:
            pprint("Unable to get songs in playlist.")
    
    def add_songs_to_playlist(self, list_of_songs):
        
        existing_songs = self.get_current_song_in_playlist()
        
        try:
            # removing duplicates which are already present
            for song in list_of_songs:
                if song in existing_songs:
                    list_of_songs.remove(song)
            
            pprint("Adding songs..")
            result = self.sp.playlist_add_items(self.playlist_id, list_of_songs)
            pprint("Added all songs..")
            
        except:
            pprint("Not able to add songs.")
            
        