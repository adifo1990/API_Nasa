from fastapi import HTTPException
from BackEnd.config import NASA_API_KEY

import requests


        
def insight_search_nasa_insight():
    try:

        response = requests.get(
            "https://api.nasa.gov/insight_weather/?",
            params={
                "api_key": NASA_API_KEY,
                "feedtype": "json",
                "version": "1.0"
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