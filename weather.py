import requests
from config import API_KEY


class Weather:

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        try:
            response = requests.get(self.BASE_URL, params=params)

            response.raise_for_status()

            data = response.json()

            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "description": data["weather"][0]["description"].title(),
                "wind_speed": data["wind"]["speed"]
            }

        except requests.exceptions.HTTPError:
            return None

        except requests.exceptions.RequestException:
            return None
