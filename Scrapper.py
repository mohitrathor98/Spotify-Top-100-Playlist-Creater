from bs4 import BeautifulSoup
import requests

class Scrapper:
    def __init__(self, date) -> None:
        self.url = f"https://www.billboard.com/charts/hot-100/{date}"
        self.soup = BeautifulSoup(self.get_html(), "html.parser")
        self.scrape()
    
    def get_html(self):
        response = requests.get(self.url)
        response.raise_for_status
        return response.text
        
    def scrape(self):
        get_song_titles = self.soup.find_all(name="h3", id="title-of-a-story")
        print(get_song_titles)