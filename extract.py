import requests
import pandas as pd
from datetime import datetime
import os

# Steam API URL for concurrent players
STEAM_API_URL = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
CONCURRENT_PLAYERS_URL = (
    "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"
)

# IGDB API settings
TOKEN_URL = "https://id.twitch.tv/oauth2/token"
IGDB_API_URL = "https://api.igdb.com/v4/games"
GENRES_API_URL = "https://api.igdb.com/v4/genres"
CLIENT_ID = "ms8zqnreo7k8v5v4fp198eivs5039o"
CLIENT_SECRET = "ia642tpku45i8qwcmp1pvo4ybi838d"


def get_access_token():
    """Request an access token from Twitch API."""
    response = requests.post(
        TOKEN_URL,
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "client_credentials",
        },
    )
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(
            f"Failed to get access token: {response.status_code} {response.text}"
        )


def fetch_igdb_data():
    """Fetch top 100 highest-rated PC games, ensuring standalone entries and removing expansions."""
    access_token = get_access_token()
    headers = {"Client-ID": CLIENT_ID, "Authorization": f"Bearer {access_token}"}
    standalone_games = []
    genres_table = []
    game_genres = []
    seen_games = set()

    # Pagination logic to ensure we get at least 100 unique standalone games
    offset = 0
    while len(standalone_games) < 100:
        query = (
            f"fields id,name,genres,rating,total_rating,total_rating_count,first_release_date; "
            f"where platforms = (6) & total_rating_count > 100 & rating > 80; "
            f"sort rating desc; limit 50; offset {offset};"
        )
        response = requests.post(IGDB_API_URL, headers=headers, data=query)
        if response.status_code != 200:
            raise Exception(
                f"IGDB API request failed: {response.status_code} {response.text}"
            )
        games = response.json()

        for game in games:
            # Skip expansions or duplicate entries (e.g., The Witcher 3 variants)
            if game["id"] in seen_games or " - " in game["name"]:
                continue

            seen_games.add(game["id"])

            # Convert first_release_date to human-readable format
            if "first_release_date" in game and game["first_release_date"]:
                game["first_release_date"] = datetime.fromtimestamp(
                    game["first_release_date"]
                ).strftime("%Y-%m-%d")

            # Handle genres
            if "genres" in game and game["genres"]:
                for genre_id in game["genres"]:
                    game_genres.append({"game_id": game["id"], "genre_id": genre_id})

            standalone_games.append(game)

        offset += 50  # Increment offset for the next page

        if not games:  # Break if no more results are returned
            break

    # Fetch genre names
    genres = fetch_genres(headers)

    # Build genres table
    genres_table = pd.DataFrame(
        list(genres.items()), columns=["genre_id", "genre_name"]
    )

    games_df = pd.DataFrame(standalone_games)
    game_genres_df = pd.DataFrame(game_genres)

    # Drop genres column from games_df
    games_df.drop(columns=["genres"], inplace=True)
    
    return games_df, genres_table, game_genres_df


def fetch_genres(headers):
    """Fetch genre names from IGDB API."""
    response = requests.post(
        GENRES_API_URL, headers=headers, data="fields id,name; limit 500;"
    )
    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch genres: {response.status_code} {response.text}"
        )
    genres = response.json()
    return {genre["id"]: genre["name"] for genre in genres}


def fetch_steam_data(games_data):
    """
    Fetch concurrent player data for the top 100 IGDB games from Steam.
    Matches IGDB games with Steam apps by name.
    """
    app_list = requests.get(STEAM_API_URL).json()["applist"]["apps"]
    steam_apps = {app["name"].lower(): app["appid"] for app in app_list}
    player_counts = []

    for _, game in games_data.iterrows():
        game_name = game["name"].lower()
        if game_name in steam_apps:
            appid = steam_apps[game_name]
            params = {"appid": appid}
            response = requests.get(CONCURRENT_PLAYERS_URL, params=params).json()
            player_counts.append(
                {
                    "game_id": game["id"],
                    "game_name": game["name"],
                    "appid": appid,
                    "current_players": response.get("response", {}).get(
                        "player_count", 0
                    ),
                }
            )

    return pd.DataFrame(player_counts)


if __name__ == "__main__":
    games_data, genres_data, game_genres_data = fetch_igdb_data()
    steam_data = fetch_steam_data(games_data)
    
    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    
    steam_data.to_csv("data/steam_data.csv", index=False)
    games_data.to_csv("data/games_data.csv", index=False)
    genres_data.to_csv("data/genres_data.csv", index=False)
    game_genres_data.to_csv("data/game_genres.csv", index=False)
