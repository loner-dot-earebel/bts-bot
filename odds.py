# odds.py

import requests
import pandas as pd

API_KEY = "2791974d9a5a94e996e61dd454eb198be23dd9adeaeede1323f39ea58502325a"

# Only two books (free-tier limit)
BOOKMAKERS = "DraftKings,FanDuel"


def implied_prob(decimal_odds):
    """Convert decimal odds to probability."""
    return 1 / float(decimal_odds)


def fetch_odds():
    """
    Pull MLB player hit props from Odds-API.io.
    Returns a dataframe:
    player | game_id | prob
    """

    url = "https://api.odds-api.io/v3/odds"

    params = {
        "apiKey": API_KEY,
        "sport": "mlb",
        "bookmakers": BOOKMAKERS
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    rows = []

    for event in data:

        game_id = event.get("id")

        # Example format from the official docs:
        # data["bookmakers"]["DraftKings"] -> list of markets
        bookmakers = event.get("bookmakers", {})

        for book_name, markets in bookmakers.items():

            for market in markets:

                # We only want "Player Props - Hits"
                if "Hits" not in market.get("name", ""):
                    continue

                for player in market.get("odds", []):

                    name = player.get("label")
                    line = player.get("hdp")
                    over_odds = player.get("over")

                    # We only want OVER 0.5 hits
                    if line != 0.5:
                        continue

                    rows.append({
                        "player": name,
                        "game_id": game_id,
                        "book": book_name,
                        "prob": implied_prob(over_odds)
                    })

    df = pd.DataFrame(rows)

    if df.empty:
        print("No hit props found")
        return df

    # Average across the 2 books
    df = (
        df.groupby(["player", "game_id"])["prob"]
        .mean()
        .reset_index()
    )

    df = df.sort_values("prob", ascending=False)

    return df
