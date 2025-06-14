import requests
from datetime import datetime, timedelta

Lon = 80.851180
Lat = 16.793719

values = {
    "latitude": Lat,
    "longitude": Lon,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=values)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_utc = datetime.fromisoformat(sunrise.replace("Z", "+00:00"))
sunset_utc = datetime.fromisoformat(sunset.replace("Z", "+00:00"))

ist_offset = timedelta(hours=5, minutes=30)
sunrise_ist = sunrise_utc + ist_offset
sunset_ist = sunset_utc + ist_offset

time_now = datetime.utcnow() + ist_offset

# Print times
print("Sunrise (IST):", sunrise_ist.strftime("%Y-%m-%d %H:%M:%S"))
print("Sunset  (IST):", sunset_ist.strftime("%Y-%m-%d %H:%M:%S"))
print("Now     (IST):", time_now.strftime("%Y-%m-%d %H:%M:%S"))

if sunrise_ist <= time_now <= sunset_ist:
    print("It's currently daytime.")
else:
    print("It's currently nighttime.")
