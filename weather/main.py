import requests

def get_weather(params):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        data = r.json()
        return data
    except Exception as ex:
        print()