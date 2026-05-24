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

def search_photos_interval(start_date: str, end_date: str):
    print("Datas recebidas buscar_asteroides:", start_date, end_date)

    url = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": API_KEY,
        "start_date": start_date,
        "end_date": end_date
    }

    print("params buscar_asteroides:", params)

    response = requests.get(url, params=params)

    print("resposta buscar_asteroides:", response)

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