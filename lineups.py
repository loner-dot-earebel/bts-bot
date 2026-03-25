import pandas as pd

def fetch_lineups():
    """
    Pulls confirmed MLB lineups.
    Returns list of confirmed player names.
    """
    # Replace with real API calls from MLB or Rotogrinders/Rotowire
    return ["Freddie Freeman","Luis Arraez","Mookie Betts"]

def filter_confirmed(df):
    confirmed = fetch_lineups()
    df = df[df['player'].isin(confirmed)]
    return df
