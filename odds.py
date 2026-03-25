import requests
import pandas as pd

def fetch_odds():
    """
    Pulls MLB player hit >0.5 props from multiple free sportsbooks.
    Returns dataframe: player, team, game_id, decimal_odds_list
    """
    # Example structure: you would replace URLs with real free APIs
    # For demo, we use placeholder data
    data = [
        {"player": "Freddie Freeman", "team": "LAD", "game_id": 1, "odds_list": [1.25,1.24,1.26]},
        {"player": "Luis Arraez", "team": "MIN", "game_id": 2, "odds_list": [1.28,1.30,1.29]},
        {"player": "Mookie Betts", "team": "LAD", "game_id": 1, "odds_list": [1.27,1.28,1.26]},
    ]
    df = pd.DataFrame(data)
    return df

def devig_and_average(df):
    """
    Converts decimal odds → implied probability, removes vig, and averages across sources
    """
    def devig(odds_list):
        probs = [1/od for od in odds_list]
        total = sum(probs)
        # devig: scale so sum=1
        probs = [p/total for p in probs]
        return sum(probs)/len(probs)
    
    df['avg_prob'] = df['odds_list'].apply(devig)
    return df[['player','team','game_id','avg_prob']]
