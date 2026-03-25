import os
from odds import fetch_odds, devig_and_average
from lineups import filter_confirmed
from weather import filter_weather
from ranking import rank_top_hitters
from notifier import send_alert
from tiebreaker import resolve_ties

def main():
    # Step 0: Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    # Step 1: Pull odds from multiple sportsbooks
    df = fetch_odds()
    df = devig_and_average(df)

    # Step 2: Filter confirmed starters
    df = filter_confirmed(df)

    # Step 3: Filter weather-risk games
    df = filter_weather(df)

    # Step 4: Resolve ties
    if not df.empty:
        df = resolve_ties(df)

    # Step 5: Rank top 3 hitters
    if not df.empty:
        top_hitters = rank_top_hitters(df, top_n=3)
    else:
        top_hitters = df  # empty DataFrame

    # Step 6: Send Telegram alert (always runs)
    send_alert(top_hitters)

    # Step 7: Save daily probabilities
    df.to_csv("data/daily_probabilities.csv", index=False)

if __name__ == "__main__":
    main()
