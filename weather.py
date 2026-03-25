def fetch_weather(game_id):
    """
    Placeholder: return True if game is safe from rain-shortened risk
    Replace with real weather API or scrape
    """
    safe_games = [1,2]  # game_ids that are safe
    return game_id in safe_games

def filter_weather(df):
    df['weather_safe'] = df['game_id'].apply(fetch_weather)
    return df[df['weather_safe']]
