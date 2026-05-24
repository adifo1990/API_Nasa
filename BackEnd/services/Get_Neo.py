from datetime import date
from datetime import datetime
import requests

API_KEY = "hzBb8xbURx2RqGRLfy8b1JrNrfIcuA2RgYbZFGWw"
URL_FEED = "https://api.nasa.gov/neo/rest/v1/feed?"
URL_LOOKUP = "https://api.nasa.gov/neo/rest/v1/neo/"
URL_BROWSE = "https://api.nasa.gov/neo/rest/v1/neo/browse"

def buscar_asteroid(
    asteroid_id: str,
    start_date: str,
    end_date: str,
    modo: str):

    print("Inf recebida:",asteroid_id, start_date ,end_date ,modo )

    url_escolhido = ""
    hoje = date.today()

    if (modo == "lookup"):
        url_escolhido = f"{URL_LOOKUP}{asteroid_id}"
        params = {
            "api_key": API_KEY
        }
    elif (modo == "feed"):

        data_inicio = datetime.strptime(start_date, "%Y-%m-%d").date()
        data_fim = datetime.strptime(end_date, "%Y-%m-%d").date()

        if(data_fim >= hoje):
            print("Data final não pode ser maior que o dia de hoje")
            return print("falhou, data final é invalida")
        
        if(data_inicio >= data_fim):
            print("Data inicial não pode ser maior que a data final")
            return print("falhou, data inicial é invalida")

        if ((data_fim - data_inicio).days >= 8):
            print("O intervalo das datas não pode ser maior que uma semana")
            return print("falhou, o intrevalo é muito grande")
    
        url_escolhido = URL_FEED
        params = {
            "api_key": API_KEY,
            "start_date": start_date,
            "end_date": end_date
        }
    elif (modo == "browse"):
        url_escolhido = URL_BROWSE
        params = {
            "api_key": API_KEY,
        }
    
    print("params:", params)
    print("Url esscolhido:", url_escolhido)

    resposta = requests.get(url_escolhido, params=params)

    print("resposta:", resposta)

    return resposta.json()