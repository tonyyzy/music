import json
from jinja2 import Template

if __name__ == "__main__":
    artists = json.load(open("test-artists.json"))["items"]
    artists = [artists[:5], artists[5:]]
    albums = json.load(open("test-tracks.json"))["items"]
    albums = [albums[:5], albums[5:]]
    with open("template.html") as f:
        template = Template(f.read())
    with open("index.html", "w") as f:
        f.write(template.render(artists=artists, albums=albums))
