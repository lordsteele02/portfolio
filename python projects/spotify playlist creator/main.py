from pprint import pprint

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "client ID here"
SPOTIPY_CLIENT_SECRET = "your key given by spotify"
URL_REDIRECT = "http://example.com"
TOKEN = "your token"

spotify = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                      client_secret=SPOTIPY_CLIENT_SECRET,
                                      redirect_uri=URL_REDIRECT,
                                      scope="playlist-modify-private",
                                      show_dialog=True,
                                      cache_path="token.txt"
                                      )


international_date_format = input(
    "Which year do you want to travel to? Type the date in format YYYY-MM-DD: ")

response = requests.get(
    f"https://www.billboard.com/charts/hot-100/{international_date_format}/")
top_hundred_webpage = response.text

soup = BeautifulSoup(top_hundred_webpage, "html.parser")
scrape_web_artist = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                                    "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                                    "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330"
                                                    " u-max-width-230@tablet-only")

scrape_web_album_name = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@"
                                                          "mobile-max u-line-height-normal@mobile-max u-letter-spacing-0"
                                                          "021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width"
                                                          "-330 u-max-width-230@tablet-only")

artist_name = []
album_name = []

for i in scrape_web_artist:
    artist_text = i.getText()
    artist_name.append(artist_text)


for i in scrape_web_album_name:
    song_text = i.getText()
    album_name.append(song_text)

stripped_artist_line = [s.strip() for s in artist_name]
stripped_album_line = [s.strip() for s in album_name]


s = spotipy.Spotify(oauth_manager=spotify)
user_id = s.current_user()["id"]


song_URIs = []
year = international_date_format.split("-")[0]

for song in stripped_artist_line:
    result = s.search(q=f"track{song} yer:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_URIs.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped")

create_playlist = s.user_playlist_create(
    user=user_id, name=f"{international_date_format} Billboard 100", public=False, description="Musical Time Machine")
s.playlist_add_items(playlist_id=create_playlist["id"], items=song_URIs)
