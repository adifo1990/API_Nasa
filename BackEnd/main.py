from fastapi import FastAPI

import requests

app = FastAPI()

API_KEY = "hzBb8xbURx2RqGRLfy8b1JrNrfIcuA2RgYbZFGWw"


@app.get("/apod/fotos")
def buscar_foto(date: str):
    print("Data recebida:", date)

    url = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": API_KEY,
        "date": date
    }

    print("params:", params)

    resposta = requests.get(url, params=params)

    print("resposta:", resposta)

    return resposta.json()