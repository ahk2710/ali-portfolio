import os, requests, pandas as pd
import matplotlib.pyplot as plt

# === INPUTS ===
airport_code = "CLT"
# NOTE: verify coords from an official source before real analysis
lat = 35.214
lon = -80.943

# ensure output dir exists INSIDE the site so Pages can serve it
out_dir = os.path.join("docs", "assets")
os.makedirs(out_dir, exist_ok=True)
out_png = os.path.join(out_dir, "001_clt_temp.png")

# fetch hourly weather (next 3 days)
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat,
    "longitude": lon,
    "hourly": "temperature_2m",
    "forecast_days": 3,
    "timezone": "auto"
}
r = requests.get(url, params=params, timeout=20)
r.raise_for_status()
data = r.json()

df = pd.DataFrame(data.get("hourly", {}))
df["time"] = pd.to_datetime(df["time"])
df = df.set_index("time")

# plot temperature
plt.figure()
df["temperature_2m"].plot(title=f"{airport_code} — Temperature (next 72h)")
plt.xlabel("Time")
plt.ylabel("Temp (°C)")
plt.tight_layout()
plt.savefig(out_png, dpi=120)
print(f"Saved chart to: {out_png}")
