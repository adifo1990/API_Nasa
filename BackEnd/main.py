from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "hzBb8xbURx2RqGRLfy8b1JrNrfIcuA2RgYbZFGWw"

@app.get("/foto/{data}")
def buscar_foto(data: str):

    url = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": API_KEY,
        "date": data
    }

    resposta = requests.get(url, params=params)

    return resposta.json()