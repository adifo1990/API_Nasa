from fastapi import HTTPException

import requests

API_KEY = "hzBb8xbURx2RqGRLfy8b1JrNrfIcuA2RgYbZFGWw"

def apod_search_nasa_photo(date: str):
    try:

        response = requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={
                "api_key": API_KEY,
                "date": date
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return data

    except requests.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Erro retornado pela NASA: {e.response.reason}"
        )

    except requests.Timeout:
        raise HTTPException(
            status_code=504,
            detail="Timeout ao acessar a API da NASA"
        )

    except ValueError:
        raise HTTPException(
            status_code=502,
            detail="Resposta inválida recebida da API da NASA"
        )

    except requests.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Falha de comunicação com a API da NASA: {str(e)}"
        )

def apod_search_nasa_photos_interval(start_date: str, end_date: str):
    try:

        response = requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={
                "api_key": API_KEY,
                "start_date": start_date,
                "end_date": end_date
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return data

    except requests.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Erro retornado pela NASA: {e.response.reason}"
        )

    except requests.Timeout:
        raise HTTPException(
            status_code=504,
            detail="Timeout ao acessar a API da NASA"
        )

    except ValueError:
        raise HTTPException(
            status_code=502,
            detail="Resposta inválida recebida da API da NASA"
        )

    except requests.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Falha de comunicação com a API da NASA: {str(e)}"
        )

def apod_search_nasa_photos_count(count: int):
    try:

        response = requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={
                "api_key": API_KEY,
                "count": count
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return data

    except requests.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Erro retornado pela NASA: {e.response.reason}"
        )

    except requests.Timeout:
        raise HTTPException(
            status_code=504,
            detail="Timeout ao acessar a API da NASA"
        )

    except ValueError:
        raise HTTPException(
            status_code=502,
            detail="Resposta inválida recebida da API da NASA"
        )

    except requests.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Falha de comunicação com a API da NASA: {str(e)}"
        )

def apod_search_nasa_photos_thumbs(thumbs: bool):
    try:

        response = requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={
                "api_key": API_KEY,
                "thumbs": thumbs
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return data

    except requests.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Erro retornado pela NASA: {e.response.reason}"
        )

    except requests.Timeout:
        raise HTTPException(
            status_code=504,
            detail="Timeout ao acessar a API da NASA"
        )

    except ValueError:
        raise HTTPException(
            status_code=502,
            detail="Resposta inválida recebida da API da NASA"
        )

    except requests.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Falha de comunicação com a API da NASA: {str(e)}"
        )