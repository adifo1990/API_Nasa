from datetime import date, datetime, timedelta

import BackEnd.rest.nasa_rest_apod as nasa_rest_apod



def apod_validate_date(date_str: str):
    
    if not date_str:
        print("Informe uma data")
        return False

    try:
        date_received = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de data inválido. Use Ano-Mes-Dia")
        return False

    min_date = date(1995, 6, 16)

    if date_received < min_date:
        print("A data deve ser maior ou igual a 1995-06-16")
        return False

    if date_received >= date.today():
        print("A data deve ser anterior à data atual")
        return False

    return True

def apod_validate_photos_interval(initial_date: str, end_date: str):
  
    if not initial_date or not end_date:
        print("Informe as datas")
        return False

    try:
        initial_date_received = datetime.strptime(initial_date, "%Y-%m-%d").date()
        end_date_received = datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de data inválido. Use Ano-Mes-Dia")
        return False

    min_date = date(1995, 6, 16)

    if initial_date_received < min_date:
        print("A data inicial deve ser maior ou igual a 1995-06-16")
        return False

    if end_date_received < min_date:
        print("A data final deve ser maior ou igual a 1995-06-16")
        return False

    if initial_date_received >= date.today():
        print("A data inicial deve ser anterior à data atual")
        return False

    if end_date_received >= date.today():
        print("A data final deve ser anterior à data atual")
        return False

    if initial_date_received > end_date_received:
        print("A data inicial não pode ser maior que a data final")
        return False

    return True

def apod_validate_count(count):
    if not count:
        print("Informe uma quantidade entre 1 e 100")
        return False

    if count < 1:
        print("A quantidade deve ser maior ou igual a 1")
        return False

    if count > 100:
        print("A quantidade deve ser menor ou igual a 100")
        return False

    return True

def apod_validate_thumbs(thumbs: bool):
    if thumbs is None:
        print("Informe o parâmetro thumbs como true ou false")
        return False

    return True

def neo_feed_validate_interval(start_date: str = None, end_date: str = None):
    
    if not start_date and end_date:
        print("Informe a data inicial (start_date)")
        return False

    if not start_date:
        print("Informe a data inicial")
        return False

    try:
        start_date_received = datetime.strptime(start_date, "%Y-%m-%d").date()
    except ValueError:
        print("Formato da data inicial inválido. Use YYYY-MM-DD")
        return False

    if start_date_received > date.today():
        print("A data inicial não pode ser maior que a data atual")
        return False

    if not end_date:
        end_date_received = start_date_received + timedelta(days=7)

        if end_date_received > date.today():
            end_date_received = date.today()
    else:
        try:
            end_date_received = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            print("Formato da data final inválido. Use YYYY-MM-DD")
            return False

        if end_date_received > date.today():
            print("A data final não pode ser maior que a data atual")
            return False

    if start_date_received > end_date_received:
        print("A data inicial não pode ser maior que a data final")
        return False

    if (end_date_received - start_date_received).days > 7:
        print("O intervalo entre as datas não pode ultrapassar 7 dias")
        return False

    return {
        "start_date": start_date_received.strftime("%Y-%m-%d"),
        "end_date": end_date_received.strftime("%Y-%m-%d")
    }

#----------------------------------------------------------------------------------------------------------------------------

def apod_search_photo(date: str):
    if not apod_validate_date(date):
        return {"error": "Data inválida"}

    return nasa_rest_apod.apod_search_nasa_photo(date)

def apod_search_photos_interval(start_date: str, end_date: str):

    if not apod_validate_photos_interval(start_date, end_date):
        return {"error": "Intervalo de datas inválido"}

    return nasa_rest_apod.apod_search_nasa_photos_interval(start_date, end_date)

def apod_search_photos_count(count: int):
    if not apod_validate_count(count):
        return {"error": "Quantidade inválida"}

    return nasa_rest_apod.apod_search_nasa_photos_count(count)

def apod_search_photos_thumbs(thumbs: bool):
    if not apod_validate_thumbs(thumbs):
        return {"error": "Parâmetro thumbs inválido"}

    return nasa_rest_apod.apod_search_nasa_photos_thumbs(thumbs)
