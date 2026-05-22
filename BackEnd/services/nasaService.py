import requests

API_KEY = "hzBb8xbURx2RqGRLfy8b1JrNrfIcuA2RgYbZFGWw"

def search_photo_APOD(date: str):
    print("Data recebida APOD:", date)

    url = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": API_KEY,
        "date": date
    }

    print("params APOD:", params)

    response = requests.get(url, params=params)

    print("resposta APOD:", response)

    return response.json()