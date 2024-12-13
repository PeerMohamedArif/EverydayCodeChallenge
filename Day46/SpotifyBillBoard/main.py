import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import os

SPOTIPY_CLIENT_ID=os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET=os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI=os.getenv("REDIRECT_URI")
USERNAME =os.getenv("USERNAME")

date=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD :")
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
url="https://www.billboard.com/charts/hot-100/"+date
response=requests.get(url=url,headers=headers)

soup=BeautifulSoup(response.text,'html.parser')
song_names_spans=soup.select("li ul li h3")
song_names=[song.getText().strip() for song in song_names_spans]


scope = "playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth
    (
        scope=scope,
        redirect_uri=REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        username=USERNAME,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uri=[]
year = date.split("-")[0]
for song in song_names:
    result=sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
