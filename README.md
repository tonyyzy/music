# music

## GET artists

GET https://api.spotify.com/v1/me/top/{type}

curl -X "GET" "https://api.spotify.com/v1/me/top/artists?time_range=short_term&limit=10&offset=0" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer #"

## GET tracks

GET https://api.spotify.com/v1/me/top/{type}

curl -X "GET" "https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=10&offset=0" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer #"