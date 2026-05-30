import requests
from enums.search_mode import SearchMode

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

URLS = {
    SearchMode.APOD.value: "https://api.nasa.gov/planetary/apod",
    SearchMode.DONKI_CME.value: "https://api.nasa.gov/DONKI/CME"
}

def search_photos_interval(start_date: str, end_date: str, search_mode: str):
    print("Datas recebidas busca intervalo:", start_date, end_date, search_mode)

    url = URLS.get(search_mode)

    params = {
        "api_key": API_KEY,
        "start_date": start_date,
        "end_date": end_date
    }

    print("params busca intervalo:", params)

    response = requests.get(url, params=params)

    print("resposta busca intervalo:", response)

    return response.json()

def search_photos_count(count: int):
    print("Contagem recebida search_photos_count:", count)

    url = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": API_KEY, 
        "count": count
    }

    print("params search_photos_count:", params)

    response = requests.get(url, params=params)

    print("resposta search_photos_count:", response)

    return response.json()       

def search_photos_thumbs(thumbs: bool):
    print("Contagem de thumbs recebida search_photos_thumbs:", thumbs)

    url = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": API_KEY, 
        "thumbs": thumbs
    }

    print("params search_photos_thumbs:", params)

    response = requests.get(url, params=params)

    print("resposta search_photos_thumbs:", response)

    return response.json()

def search_photos_interval_donki(start_date: str, end_date: str, search_mode: str):
    print("Datas recebidas buscar_asteroides_donki:", start_date, end_date)

    url = "https://api.nasa.gov/DONKI/CME"

    params = {
        "api_key": API_KEY,
        "start_date": start_date,
        "end_date": end_date
    }

    print("params buscar_asteroides_donki:", params)

    response = requests.get(url, params=params)

    print("resposta buscar_asteroides_donki:", response)

    return response.json()