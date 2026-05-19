import requests

API_KEY = "hzBb8xbURx2RqGRLfy8b1JrNrfIcuA2RgYbZFGWw"

def search_photo(date: str):
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

def search_asteroids(start_date: str, end_date: str):
    print("Datas recebidas buscar_asteroides:", start_date, end_date)

    url = "https://api.nasa.gov/neo/rest/v1/feed"

    params = {
        "api_key": API_KEY,
        "start_date": start_date,
        "end_date": end_date
    }

    print("params buscar_asteroides:", params)

    response = requests.get(url, params=params)

    print("resposta buscar_asteroides:", response)

    return response.json()