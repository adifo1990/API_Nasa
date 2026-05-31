from urllib import response

import requests
#from enums.search_mode import SearchMode

API_KEY = "hzBb8xbURx2RqGRLfy8b1JrNrfIcuA2RgYbZFGWw"

def apod_search_nasa_photo(date: str):
    try:
        print("1 - Iniciando requisição NASA")

        response = requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={
                "api_key": API_KEY,
                "date": date
            },
            timeout=30
        )

        print("2 - Requests retornou")

        response.raise_for_status()

        print("3 - Status OK")

        data = response.json()

        print("4 - JSON convertido")

        print(f"Quantidade de fotos retornadas: {len(data)}")

        return data

    except requests.HTTPError as e:
        return {
            "success": False,
            "status_code": e.response.status_code,
            "message": e.response.reason
        }

    except requests.Timeout:
        return {
            "success": False,
            "message": "Timeout ao acessar a API da NASA"
        }

    except requests.RequestException as e:
        return {
            "success": False,
            "message": str(e)
        }

def apod_search_nasa_photos_interval(start_date: str, end_date: str):
    try:
        print("1 - Iniciando requisição NASA (intervalo)")

        response = requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={
                "api_key": API_KEY,
                "start_date": start_date,
                "end_date": end_date
            },
            timeout=30
        )

        print("2 - Requests retornou")

        response.raise_for_status()

        print("3 - Status OK")

        data = response.json()

        print("4 - JSON convertido")
        print(f"Quantidade de fotos retornadas: {len(data)}")


        return data

    except requests.HTTPError as e:
        return {
            "success": False,
            "status_code": e.response.status_code,
            "message": e.response.reason
        }

    except requests.Timeout:
        return {
            "success": False,
            "message": "Timeout ao acessar a API da NASA"
        }

    except requests.RequestException as e:
        return {
            "success": False,
            "message": str(e)
        }

def apod_search_nasa_photos_count(count: int):
    try:
        print("1 - Iniciando requisição NASA (count)")

        response = requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={
                "api_key": API_KEY,
                "count": count
            },
            timeout=30
        )

        print("2 - Requests retornou")

        response.raise_for_status()

        print("3 - Status OK")

        data = response.json()

        print("4 - JSON convertido")

        print(f"Quantidade de fotos retornadas: {len(data)}")

        return data

    except requests.HTTPError as e:
        return {
            "success": False,
            "status_code": e.response.status_code,
            "message": e.response.reason
        }

    except requests.Timeout:
        return {
            "success": False,
            "message": "Timeout ao acessar a API da NASA"
        }

    except requests.RequestException as e:
        return {
            "success": False,
            "message": str(e)
        }

def apod_search_nasa_photos_thumbs(thumbs: bool):
    try:
        print("1 - Iniciando requisição NASA (thumbs)")

        response = requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={
                "api_key": API_KEY,
                "thumbs": thumbs
            },
            timeout=30
        )

        print("2 - Requests retornou")

        response.raise_for_status()

        print("3 - Status OK")

        data = response.json()

        print("4 - JSON convertido")

        print(f"Thumbs solicitado: {thumbs}")

        return data

    except requests.HTTPError as e:
        return {
            "success": False,
            "status_code": e.response.status_code,
            "message": e.response.reason
        }

    except requests.Timeout:
        return {
            "success": False,
            "message": "Timeout ao acessar a API da NASA"
        }

    except requests.RequestException as e:
        return {
            "success": False,
            "message": str(e)
        }

#def donki_search_nasa_photos_interval(start_date: str, end_date: str):
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