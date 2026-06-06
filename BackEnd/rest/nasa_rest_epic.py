from fastapi import HTTPException

import requests

API_KEY = "hzBb8xbURx2RqGRLfy8b1JrNrfIcuA2RgYbZFGWw"

def epic_search_nasa_epic_natural():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/natural",
            params={
                "api_key": API_KEY
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

def epic_search_nasa_epic_natural_by_date(date: str):
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/natural/date/{date}".format(date=date),
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_natural_all():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/natural/all",
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_natural_available():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/natural/available",
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_enhanced():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/enhanced",
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_enhanced_by_date(date: str):
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/enhanced/date/{date}".format(date=date),
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_enhanced_all():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/enhanced/all",
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_enhanced_available():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/enhanced/available",
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_aerosol():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/aerosol",
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_aerosol_by_date(date: str):
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/aerosol/date/{date}".format(date=date),
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_aerosol_all():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/aerosol/all",
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_aerosol_available():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/aerosol/available",
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_cloud():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/cloud",
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_cloud_by_date(date: str):
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/cloud/date/{date}".format(date=date),
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_cloud_all():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/cloud/all",
            params={
                "api_key": API_KEY
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
        
def epic_search_nasa_epic_cloud_available():
    try:
        response = requests.get(
            "https://api.nasa.gov/EPIC/api/cloud/available",
            params={
                "api_key": API_KEY
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