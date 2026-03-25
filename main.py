# main.py
from odds import fetch_odds, devig_and_average
from lineups import filter_confirmed
from weather import filter_weather
from ranking import rank_top_hitters
from notifier import send_alert
from tiebreaker import resolve_ties
import pandas as pd

def main():
    # Step 1: Pull odds from multiple sportsbooks
    df = fetch_odds()
    df = devig_and_average(df)

    # Step 2: Filter confirmed starters
    df = filter_confirmed(df)

    # Step 3: Filter weather-risk games (any realistic shortened-game risk)
    df = filter_weather(df)

    # Step 4: Resolve ties using your hierarchy
    df = resolve_ties(df)

    # Step 5: Rank top 3 hitters
    top_hitters = rank_top_hitters(df, top_n=3)

    # Step 6: Send Telegram alert
    send_alert(top_hitters)

    # Step 7: Save daily probabilities for future baseline
    df.to_csv("data/daily_probabilities.csv", index=False)

if __name__ == "__main__":
    main()
