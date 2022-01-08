from Scrapper import Scrapper
from spotify import Spotify

date = input("Which date's top 100 songs do you want? Enter date in this format YYYY-MM-DD: ")
scrape = Scrapper(date)
song_list = scrape.scrape()

sp = Spotify()

list_of_songs = sp.create_list(song_list, date)

sp.create_playlist(date)
sp.add_songs_to_playlist(list_of_songs)