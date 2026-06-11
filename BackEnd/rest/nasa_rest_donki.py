from fastapi import HTTPException
from BackEnd.config import NASA_API_KEY

import requests

def donki_cme_search_nasa_cme(start_date: str, end_date: str):
    try:
        
        response = requests.get(
            "https://api.nasa.gov/DONKI/CME",
            params={
                "api_key": NASA_API_KEY,
                "startDate": start_date,
                "endDate": end_date
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

def donki_cme_analysis_search_nasa_cme_analysis(start_date: str, end_date: str, most_accurate_only: bool, complete_entry_only: bool, speed: int, half_angle: int, catalog: str, keyword: str):
    try:

        response = requests.get(
            "https://api.nasa.gov/DONKI/CMEAnalysis",
            params={
                "api_key": NASA_API_KEY,
                "startDate": start_date,
                "endDate": end_date,
                "most_accurate_only": most_accurate_only,
                "complete_entry_only": complete_entry_only,
                "speed": speed,
                "half_angle": half_angle,
                "catalog": catalog,
                "keyword": keyword
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
        
def donki_gst_search_nasa_gst(start_date: str, end_date: str):
    try:
        
        response = requests.get(
            "https://api.nasa.gov/DONKI/GST",
            params={
                "api_key": NASA_API_KEY,
                "startDate": start_date,
                "endDate": end_date
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
        
def donki_ips_search_nasa_ips(start_date: str, end_date: str, location: str, catalog: str):
    try:
    
        response = requests.get(
            "https://api.nasa.gov/DONKI/IPS",
            params={
                "api_key": NASA_API_KEY,
                "startDate": start_date,
                "endDate": end_date,
                "location": location,
                "catalog": catalog
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
        
def donki_flr_search_nasa_flr(start_date: str, end_date: str): 
    try:

        response = requests.get(
            "https://api.nasa.gov/DONKI/FLR",
            params={
                "api_key": NASA_API_KEY,
                "startDate": start_date,
                "endDate": end_date
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
        
def donki_sep_search_nasa_sep(start_date: str, end_date: str):
    try:
        
        response = requests.get(
            "https://api.nasa.gov/DONKI/SEP",
            params={
                "api_key": NASA_API_KEY,
                "startDate": start_date,
                "endDate": end_date
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
                
def donki_mpc_search_nasa_mpc(start_date: str, end_date: str):
    try:

        response = requests.get(
            "https://api.nasa.gov/DONKI/MPC",
            params={
                "api_key": NASA_API_KEY,
                "startDate": start_date,
                "endDate": end_date
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
        
def donki_rbe_search_nasa_rbe(start_date: str, end_date: str):
    try:

        response = requests.get(
            "https://api.nasa.gov/DONKI/RBE",
            params={
                "api_key": NASA_API_KEY,
                "startDate": start_date,
                "endDate": end_date
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
        
def donki_hss_search_nasa_hss(start_date: str, end_date: str):
    try:
        
        response = requests.get(
            "https://api.nasa.gov/DONKI/HSS",
            params={
                "api_key": NASA_API_KEY,
                "startDate": start_date,
                "endDate": end_date
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
        
def donki_wsaenlilsimulation_search_nasa_wsaenlilsimulation(start_date: str, end_date: str):
    try:
        
        response = requests.get(
            "https://api.nasa.gov/DONKI/WSAEnlilSimulations",
            params={
                "api_key": NASA_API_KEY,
                "startDate": start_date,
                "endDate": end_date
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
        
def donki_notification_search_nasa_notification(start_date: str, end_date: str, type: str):
    try:

        response = requests.get(
            "https://api.nasa.gov/DONKI/notifications",
            params={
                "api_key": NASA_API_KEY,
                "startDate": start_date,
                "endDate": end_date,
                "type": type
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