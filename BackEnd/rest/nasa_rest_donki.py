from http.client import HTTPException

import requests

API_KEY = "hzBb8xbURx2RqGRLfy8b1JrNrfIcuA2RgYbZFGWw"

def donki_cme_search_nasa_cme(start_date: str, end_date: str):
    try:
        print("1 - Iniciando requisição NASA (intervalo)")

        response = requests.get(
            "https://api.nasa.gov/neo/rest/v1/feed",
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
