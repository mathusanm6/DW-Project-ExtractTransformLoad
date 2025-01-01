import pandas as pd
import sqlite3
import os


def load_to_sqlite():
    """Load transformed data into SQLite."""
    db_path = "db/games_data.db"
    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect("db/games_data.db")
    final_data = pd.read_csv("data/final_data.csv")
    genres_data = pd.read_csv("data/genres_data.csv")
    game_genres_data = pd.read_csv("data/game_genres.csv")

    final_data.to_sql("games", conn, if_exists="replace", index=False)
    genres_data.to_sql("genres", conn, if_exists="replace", index=False)
    game_genres_data.to_sql("game_genres", conn, if_exists="replace", index=False)

    conn.close()


if __name__ == "__main__":
    load_to_sqlite()
