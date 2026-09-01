import requests


def get_weather():
    response = requests.get(
        "https://api.weather.com/current"
    )

    return response.json()

