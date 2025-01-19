import pandas as pd
import sqlite3
import plotly.express as px


def create_dashboard():
    """Visualize data from SQLite database."""
    conn = sqlite3.connect("db/games_data.db")

    # Load data
    games_with_genres = pd.read_sql("SELECT * FROM games", conn)

    # Aggregate ratings by genre
    avg_ratings = games_with_genres.groupby("Genre Name")["Rating"].mean().reset_index()
    avg_ratings = avg_ratings.sort_values(by="Rating", ascending=False)
    
    # Calculate average player counts by genre
    avg_players_by_genre = (
        games_with_genres.groupby("Genre Name")["Current Players"]
        .mean()
        .reset_index()
    ).sort_values(by='Current Players', ascending=False)

    avg_engagement_score_by_genre = (
        games_with_genres.groupby("Genre Name")["Engagement Score"]
        .mean()
        .reset_index()
    ).sort_values(by='Engagement Score', ascending=False)


    # Create a bar chart
    fig = px.bar(
        avg_ratings,
        x="Genre Name",
        y="Rating",
        title="Average Rating by Genre",
        labels={"Genre Name": "Genre", "Rating": "Average Rating"},
        color="Rating",
        color_continuous_scale="Viridis",
        template="simple_white",
    )

    # Update layout for better aesthetics
    fig.update_layout(
        title_font=dict(size=22, family="Arial", color="darkblue"),
        xaxis_title_font=dict(size=16, family="Arial", color="black"),
        yaxis_title_font=dict(size=16, family="Arial", color="black"),
        xaxis_tickangle=-45,
        margin=dict(l=50, r=50, t=100, b=100),
        coloraxis_colorbar=dict(
            title="Rating",
            title_font=dict(size=14, family="Arial"),
            tickfont=dict(size=12, family="Arial"),
        ),
    )

    fig.show()

    fig2 = px.bar(
        avg_players_by_genre,
        x="Genre Name",
        y="Current Players",
        title="Average Numbers of player by Genre",
        labels={"Genre Name": "Genre", "Current Players": "Average Nums Player"},
        color="Current Players",
        color_continuous_scale="Viridis",
        template="simple_white"
    )
    fig2.show()
    
    fig_scatter = px.scatter(
        games_with_genres,
        x="Current Players",
        y="Engagement Score",
        size="Rating Count",
        color="Total Rating With Critic Reviews",
        hover_name="Game Name",
        title="Engagement Score vs Current Players",
        labels={
            "Current Players": "Current Players",
            "Engagement Score": "Engagement Score",
            "Total Rating With Critic Reviews": "Total Rating",
            "Rating Count": "Number of Ratings"
        },
        template="plotly_white",
        color_continuous_scale="Plasma"
    )

    fig_scatter.update_layout(
        title_font=dict(size=22, family="Arial", color="darkblue"),
        xaxis_title_font=dict(size=16, family="Arial", color="black"),
        yaxis_title_font=dict(size=16, family="Arial", color="black"),
        margin=dict(l=50, r=50, t=100, b=100),
        legend_title=dict(font=dict(size=14, family="Arial"))
    )

    fig_scatter.show()

    

    conn.close()


if __name__ == "__main__":
    create_dashboard()
