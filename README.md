# Spotify-Top-100-Playlist-Creater
Fetches top 100 songs for any specified date and creates playlist on spotify.

## Requirement
1) Python 3.5+
2) Spotify Account

## Working

### Getting Spotify ID and Secret Code
1) Go to <a href="https://developer.spotify.com/dashboard/">Spotify Developer</a>
2) Create an app and get your client ID and secret code
3) Paste those in spotify.py file(in init() method).

### Running
<ul><li>Run using python3/python main.py</li>
<li>Give date in YYYY-MM-DD format to create a playlist of top 100 songs on that day.</li></ul>

### Getting Top 100 Songs
<ul><li>Billboard charts are being used to get top 100 songs at any given data</li></ul>

### Spotify Playlist Creation
<ul>
<li>Using Spotipy python library to interact with Spotify APIs</li>
<li>Spotify Client ID and Client sectet code is required</li>
<li>Playlist Name will be: "Given_Date Billboard 100"</li>
<li>Playlist will be public.</li>
</ul>



