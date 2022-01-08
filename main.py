from Scrapper import Scrapper
from spotify import Spotify

date = "2016-07-31"#input("Which date's top 100 songs do you want? Enter date in this format YYYY-MM-DD: ")
scrape = Scrapper(date)
song_list = scrape.scrape()

sp = Spotify()

#list_of_songs = sp.create_list(song_list, date)
#print(list_of_songs)

sp.create_playlist(date)