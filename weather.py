import requests

def fetch_weather(game_id):
    """Return True if game is safe from being shortened by rain."""
    # Example using OpenWeatherMap free API
    API_KEY = "YOUR_OPENWEATHER_API_KEY"
    # You need latitude/longitude for the stadium
    lat, lon = get_stadium_coords(game_id)
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
    r = requests.get(url).json()
    for hour in r['list']:
        if hour['pop'] > 0.4:  # >40% chance of precipitation
            return False
    return True

def filter_weather(df):
    safe_games = []
    for i, row in df.iterrows():
        if fetch_weather(row['game_id']):
            safe_games.append(row)
    return pd.DataFrame(safe_games)
