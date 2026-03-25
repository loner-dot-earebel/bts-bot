import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_odds():
    """Scrape or fetch MLB player prop odds for hits."""
    url = "https://www.oddsjam.com/mlb/player-props/hits"  # example, adjust
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    players = []
    # Example parsing logic, depends on site structure
    for row in soup.select(".player-row"):
        player = row.select_one(".player-name").text.strip()
        team = row.select_one(".team").text.strip()
        odds_text = row.select_one(".odds").text.strip()
        odds = [float(x) for x in odds_text.split("/")]  # convert to decimal or implied
        players.append({"player": player, "team": team, "odds_list": odds})

    df = pd.DataFrame(players)
    # Devig and average odds across books
    df['avg_prob'] = df['odds_list'].apply(lambda x: sum([1/odd for odd in x])/len(x))
    return df[['player','team','avg_prob']]
