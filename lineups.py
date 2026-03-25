import requests
from bs4 import BeautifulSoup

def get_confirmed_lineups():
    url = "https://www.rotogrinders.com/lineups/mlb"  # example
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    confirmed_players = []
    for player_tag in soup.select(".player-name"):
        confirmed_players.append(player_tag.text.strip())
    return confirmed_players

def filter_confirmed(df):
    starters = get_confirmed_lineups()
    df = df[df['player'].isin(starters)]
    return df
