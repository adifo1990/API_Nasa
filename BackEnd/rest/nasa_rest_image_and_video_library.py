from fastapi import HTTPException
from BackEnd.config import NASA_API_KEY

import requests


        
def image_and_video_library_search(q: str, center: str = None, description: str = None, description_508: str = None,
                                   keywords: str = None, location: str = None, media_type: str = None, nasa_id: str = None,
                                   page: int = None, page_size: int = None, photographer: str = None,
                                   secondary_creator: str = None, title: str = None, year_start: str = None, year_end: str = None):

    try:

        response = requests.get(
            "https://images-api.nasa.gov/search",
            params={
                "q": q,
                "center": center,
                "description": description,
                "description_508": description_508,
                "keywords": keywords,
                "location": location,
                "media_type": media_type,
                "nasa_id": nasa_id,
                "page": page,
                "page_size": page_size,
                "photographer": photographer,
                "secondary_creator": secondary_creator,
                "title": title,
                "year_start": year_start,
                "year_end": year_end
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