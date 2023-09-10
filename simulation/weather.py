import requests

endpoints = {
  "current": "/data/2.5/weather",
  "history": "data/2.5/history/city",
  "forecast": "/data/2.5/forecast",
  "geocoding": "/geo/1.0/direct",
}

location = {
  "name": "Null Island",
  "coord": {
    "lat": 0.0,
    "lon": 0.0,
  }
}

def weather(endpoint: str, **params: str):
  return requests.get(f"https://api.openweathermap.org{endpoints[endpoint]}", params={
    "appid": "OPENWEATHER API KEY",
    "units": "metric",
    **location["coord"],
    **params,
  }).json()

def geocode(loc: str, update=True):
  global location
  data: dict = weather("geocoding", q=loc, limit=1)[0]
  pos = {
    "name": data["name"],
    "country": data["country"],
    "state": data.get("state"),
    "coord": {
      "lat": data["lat"],
      "lon": data["lon"]
    }
  }
  if update: location = pos
  return pos
