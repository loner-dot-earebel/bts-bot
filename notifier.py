import requests

TELEGRAM_BOT_TOKEN = "8639278401:AAGM9aj28jl9qPO9nvkGBLc6AnhawuYZuxk"
CHAT_ID = "8674257644"

def send_alert(top_hitters):
    if top_hitters.empty:
        text = "NO SAFE PICKS TODAY\nTop hitters all in weather-risk games or lineup not confirmed early enough"
    else:
        text = "BTS PICKS READY\n\n"
        for i, row in enumerate(top_hitters.itertuples(),1):
            text += f"#{i} {row.player} — {row.avg_prob*100:.1f}%\n"
        text += "\nAll confirmed in lineups\nAll weather-safe games\nNOTE: Historical baseline not yet available; use judgment for double-down."
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})
