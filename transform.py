import numpy as np
import pandas as pd


def transform_data():
    """Merge and clean Steam and IGDB data."""
    steam_data = pd.read_csv("data/steam_data.csv")
    games_data = pd.read_csv("data/games_data.csv")
    game_genres_data = pd.read_csv("data/game_genres.csv")
    genres_data = pd.read_csv("data/genres_data.csv")

    # Merge on game id
    merged_data = pd.merge(
        steam_data, games_data, left_on="game_id", right_on="id", how="inner"
    )
    assert(merged_data['id'].is_unique==True)

    # Join with game_genres_data to associate genres with games
    merged_data_with_genres = pd.merge(
        merged_data,
        game_genres_data,
        left_on="game_id",
        right_on="game_id",
        how="inner",
    )
    merged_data_with_genres = pd.merge(
        merged_data_with_genres,
        genres_data,
        left_on="genre_id",
        right_on="genre_id",
        how="inner",
    )

    # Calculate average player counts by genre
    avg_players_by_genre = (
        merged_data_with_genres.groupby("genre_name")["current_players"]
        .mean()
        .reset_index()
    )

    # Calculate engagement score
    merged_data["engagement_score"] = merged_data["rating"] * np.log1p(merged_data["current_players"])


    # Drop unnecessary columns
    merged_data.drop(columns=["name", "id"], inplace=True)

    # Reorganize columns with coherent order and names
    merged_data = merged_data[
        [
            "game_id",
            "game_name",
            "appid",
            "first_release_date",
            "current_players",
            "rating",
            "total_rating",
            "total_rating_count",
            "engagement_score",
        ]
    ]
    merged_data.rename(
        columns={
            "game_id": "IGDB Game ID",
            "game_name": "Game Name",
            "appid": "Steam App ID",
            "current_players": "Current Players",
            "first_release_date": "Release Date",
            "rating": "Rating",
            "total_rating": "Total Rating With Critic Reviews",
            "total_rating_count": "Rating Count",
            "engagement_score": "Engagement Score",
        },
        inplace=True,
    )

    return merged_data, avg_players_by_genre


if __name__ == "__main__":
    final_data, genre_insights = transform_data()
    final_data.to_csv("data/final_data.csv", index=False)
    genre_insights.to_csv("data/genre_insights.csv", index=False)
