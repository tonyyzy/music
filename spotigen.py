import sys
from jinja2 import Template
import spotipy

if __name__ == "__main__":
    token = sys.argv[1]
    sp = spotipy.Spotify(auth=token)
    artists = sp.current_user_top_artists(time_range="short_term", limit=10)["items"]
    artists = [artists[:5], artists[5:]]
    albums = sp.current_user_top_tracks(time_range="short_term", limit=10)["items"]
    albums = [albums[:5], albums[5:]]
    with open("template.html") as f:
        template = Template(f.read())
    with open("index.html", "w") as f:
        f.write(template.render(artists=artists, albums=albums))
