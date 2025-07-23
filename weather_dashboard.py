import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

API_KEY = "276d7bab6223366e6358b74a49e981bc"  # Replace with your real key
CITY = "Mumbai"
UNITS = "metric"

def fetch_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city,
        'appid': api_key,
        'units': UNITS
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def parse_weather_data(data):
    timestamps = []
    temps = []
    humidities = []

    for entry in data['list']:
        dt = datetime.fromtimestamp(entry['dt'])
        temp = entry['main']['temp']
        humidity = entry['main']['humidity']

        timestamps.append(dt)
        temps.append(temp)
        humidities.append(humidity)

    return timestamps, temps, humidities

def plot_weather(timestamps, temps, humidities):
    sns.set(style="whitegrid")

    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    sns.lineplot(x=timestamps, y=temps, marker='o', color='orangered')
    plt.title("Temperature Forecast")
    plt.xlabel("Date/Time")
    plt.ylabel("Temp (°C)")
    plt.xticks(rotation=45)

    plt.subplot(1, 2, 2)
    sns.lineplot(x=timestamps, y=humidities, marker='o', color='steelblue')
    plt.title("Humidity Forecast")
    plt.xlabel("Date/Time")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

# --- Main ---
if __name__ == "__main__":
    print(f"Fetching data for {CITY}...")
    data = fetch_weather_data(CITY, API_KEY)
    timestamps, temps, humidities = parse_weather_data(data)
    plot_weather(timestamps, temps, humidities)
