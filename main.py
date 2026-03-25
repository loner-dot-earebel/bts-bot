from odds import fetch_odds, devig_and_average
from lineups import filter_confirmed
from weather import filter_weather
from ranking import rank_top_hitters
from notifier import send_alert
import pandas as pd

def main():
    # Step 1: Pull odds
    df = fetch_odds()
    df = devig_and_average(df)
    
    # Step 2: Filter confirmed starters
    df = filter_confirmed(df)
    
    # Step 3: Filter weather-risk games
    df = filter_weather(df)
    
    # Step 4: Rank top 3 hitters
    top_hitters = rank_top_hitters(df, top_n=3)
    
    # Step 5: Send Telegram alert
    send_alert(top_hitters)
    
    # Step 6: Save daily probabilities
    df.to_csv("data/daily_probabilities.csv", index=False)

if __name__ == "__main__":
    main()
