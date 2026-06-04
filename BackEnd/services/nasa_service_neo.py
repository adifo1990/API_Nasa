from datetime import date, datetime

import BackEnd.rest.nasa_rest_neo as nasa_rest_neo


def neo_feed_validate_interval(start_date: str, end_date: str):

    if not start_date or not end_date:
        return False

    try:
        start_date_received = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date_received = datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        return False

    if start_date_received > date.today():
        return False
    
    if end_date_received > date.today():
        return False

    if start_date_received > end_date_received:
        return False

    if (end_date_received - start_date_received).days > 7:
        return False

    return True

def neo_lookup_validate_asteroid_id(asteroid_id: int):
    if not asteroid_id:
        return False

    if not asteroid_id >= 0:
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