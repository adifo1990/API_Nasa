from datetime import date, datetime

import BackEnd.rest.nasa_rest_donki as nasa_rest_donki


def donki_cme_validate_interval(start_date: str, end_date: str):

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


#----------------------------------------------------------------------------------------------------------------------------

def donki_cme_search_interval(start_date: str, end_date: str):
    if not donki_cme_validate_interval(start_date, end_date):
        return {"error": "Intervalo de datas inválido"}

    return nasa_rest_donki.donki_cme_search_nasa_cme(start_date, end_date)
