import requests, pandas as pd

# === INPUTS ===
airport_code = "CLT"
# TODO: verify official coordinates before trusting these in any analysis
lat = 35.214   # placeholder: verify
lon = -80.943  # placeholder: verify

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat,
    "longitude": lon,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m,visibility",
    "forecast_days": 3,
    "timezone": "auto"
}

r = requests.get(url, params=params, timeout=20)
r.raise_for_status()
data = r.json()

hourly = data.get("hourly", {})
df = pd.DataFrame(hourly)
df["time"] = pd.to_datetime(df["time"])

print(f"{airport_code} hourly weather — first 5 rows:")
print(df.head(5))
