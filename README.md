# 🎧 Spotify Top Tracks 2023 | Power BI + Spotify Web API

Power BI dashboard on the most-streamed Spotify songs of 2023. A Python script enriches the track dataset with album cover URLs pulled from the Spotify Web API, so the report can show artwork next to streams, chart presence and audio features like danceability and energy.

## Stack
`Power BI` `Python` `pandas` `requests` `tqdm` `Spotify Web API` `CSV`

## What it does
- Loads `Data_script/spotify-2023.csv` (953 tracks) with streams, playlist and chart counts across Spotify, Apple Music, Deezer and Shazam.
- Authenticates with the Spotify Web API (client credentials flow), searches each track by name and lead artist, and stores the album cover URL in a new `image_url` column (`Data_script/updated_file1.csv`).
- Visualizes streams per track, release timeline and audio features (BPM, key, mode, danceability, valence, energy, acousticness and more) in `SpotifyBI.pbix`.
- Uses a custom Office theme, logo and backgrounds from `imgs/` (`Theme1.thmx`, `Logo1.png`, `Layout-BG.png`, `BackGround.pptx`).

## How to open / run
1. Clone the repo:
   ```bash
   git clone https://github.com/lucas-wall/API-Spotify-BI.git
   ```
2. To just view the report, open `SpotifyBI.pbix` in Power BI Desktop and, if prompted, point the source to `Data_script/updated_file1.csv`.
3. To regenerate the enriched CSV:
   - Create an app in the Spotify Developer Dashboard to get a client ID and secret.
   - In `Data_script/Spotify_script1.py`, remove the triple quotes around the API block and fill in `CLIENT_ID` and `CLIENT_SECRET`.
   - Install dependencies and run it from the `Data_script/` folder:
     ```bash
     pip install pandas requests tqdm
     cd Data_script
     python Spotify_script1.py
     ```
4. Refresh the Power BI report to pick up the new `updated_file1.csv`.

## Repo layout
- `SpotifyBI.pbix` - the Power BI report
- `Data_script/` - enrichment script, source CSV and enriched outputs
- `imgs/` - theme, logo and background assets
