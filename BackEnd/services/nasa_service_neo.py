from datetime import date, datetime

import BackEnd.rest.nasa_rest_neo as nasa_rest_neo


def neo_feed_validate_interval(start_date: str, end_date: str):

    if not start_date or not end_date:
        print("Informe as datas")
        return False

    try:
        start_date_received = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date_received = datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de data inválido. Use Ano-Mes-Dia")
        return False

    if start_date_received > date.today():
        print("A data inicial deve ser anterior à data atual")
        return False
    
    if end_date_received > date.today():
        print("A data final deve ser anterior à data atual")
        return False

    if start_date_received > end_date_received:
        print("A data inicial não pode ser maior que a data final")
        return False

    if (end_date_received - start_date_received).days > 7:
        print("O intervalo entre as datas não pode ultrapassar 7 dias")
        return False

    return True

def neo_lookup_validate_asteroid_id(asteroid_id: int):
    if not asteroid_id:
        print("Informe o ID do asteroide")
        return False

    if not asteroid_id >= 0:
        print("O ID do asteroide deve ser maior ou igual a zero")
        return False

    return True

#----------------------------------------------------------------------------------------------------------------------------

def neo_feed_search_interval(start_date: str, end_date: str):
    if not neo_feed_validate_interval(start_date, end_date):
        return {"error": "Intervalo de datas inválido"}

    return nasa_rest_neo.neo_feed_search_nasa_asteroids_interval(start_date, end_date)

def neo_lookup_search(asteroid_id: int):
    if not neo_lookup_validate_asteroid_id(asteroid_id):
        return {"error": "ID do asteroide inválido"}

    return nasa_rest_neo.neo_lookup_search_nasa_asteroid(asteroid_id)
    
def neo_browse_search():

    return nasa_rest_neo.neo_browse_search_nasa_asteroids()