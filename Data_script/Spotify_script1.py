import base64
import json
import pandas as pd
import requests
from tqdm import tqdm

# Note: the API enrichment block below is wrapped in a triple-quoted string so it does not
# re-query the Spotify API on every run. To re-run it, remove the triple quotes and set
# CLIENT_ID / CLIENT_SECRET with your own Spotify Developer credentials.

'''# Initialize your client ID and client secret from Spotify Developer Dashboard
CLIENT_ID = '--'
CLIENT_SECRET = '--'

def get_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_song_url(track_name, artist_name, headers):
    search_url = 'https://api.spotify.com/v1/search'
    query = f'{track_name} artist:{artist_name}'
    response = requests.get(search_url, headers=headers, params={'q': query, 'type': 'track', 'limit': 1})
    results = response.json()
    items = results['tracks']['items']
    if items:
        album_image_url = items[0]['album']['images'][0]['url'] if items[0]['album']['images'] else None
        return album_image_url
    else:
        return None, None


# Load your CSV file
df_spotify = pd.read_csv('spotify-2023.csv', encoding='latin1')

# Get Spotify access token and headers
access_token = get_token()
headers = get_auth_header(access_token)

# Initialize an empty list to store Spotify URLs
#spotify_urls = []
image_urls = []
# Iterate over each row in the DataFrame with tqdm for progress tracking
for _, row in tqdm(df_spotify.iterrows(), total=len(df_spotify)):
    url = get_song_url(row['track_name'], row['artist(s)_name'].split(',')[0], headers)
    image_urls.append(url)

# Add the collected URLs as a new column to the DataFrame
#df_spotify['spotify_url'] = spotify_urls
df_spotify['image_url'] = image_urls


'''# Save the updated DataFrame to a new CSV file


df_spotify.to_csv('updated_file1.csv', index=False, encoding='latin1')