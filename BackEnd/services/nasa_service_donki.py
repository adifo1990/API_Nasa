from datetime import date, datetime, timedelta

import BackEnd.rest.nasa_rest_donki as nasa_rest_donki


def donki_cme_validate_interval(start_date: str, end_date: str):

    if not start_date:
        start_date = (date.today() - timedelta(days=30)).strftime("%Y-%m-%d")

    if not end_date:
        end_date = date.today().strftime("%Y-%m-%d")

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

    return True

def donki_cme_analysis_validate(start_date: str, end_date: str, most_accurate_only: bool, 
                                complete_entry_only: bool, speed: int, half_angle: int, catalog: str, keyword: str):

    if not start_date:
        start_date = (date.today() - timedelta(days=30)).strftime("%Y-%m-%d")

    if not end_date:
        end_date = date.today().strftime("%Y-%m-%d")

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
    
    if most_accurate_only is None:
        most_accurate_only = True

    if not isinstance(most_accurate_only, bool):
        return False

    if complete_entry_only is None:
        complete_entry_only = True

    if not isinstance(complete_entry_only, bool):
        return False

    if speed is None:
        speed = 0

    if speed < 0:
        return False

    if half_angle is None:
        half_angle = 0

    if half_angle < 0:
        return False

    if not catalog:
        catalog = "ALL"

    catalogs_validos = [
        "ALL",
        "SWRC_CATALOG",
        "JANG_ET_AL_CATALOG"
    ]

    if catalog not in catalogs_validos:
        return False

    if not keyword:
        keyword = "NONE"

    return True

def donki_gst_validate_interval(start_date: str, end_date: str):

    if not start_date:
        start_date = (date.today() - timedelta(days=30)).strftime("%Y-%m-%d")

    if not end_date:
        end_date = date.today().strftime("%Y-%m-%d")

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

    return True

def donki_ips_validate_interval(start_date: str, end_date: str, location: str, catalog: str):
    
    if not start_date:
        start_date = (date.today() - timedelta(days=30)).strftime("%Y-%m-%d")

    if not end_date:
        end_date = date.today().strftime("%Y-%m-%d")

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
    
    if not location:
        location = "ALL"

    locations_validas = [
        "ALL",
        "Earth",
        "STEREO A",
        "STEREO B",
        "ACE",
        "Wind"
    ]

    if location not in locations_validas:
        return False

    if not catalog:
        catalog = "ALL"

    catalogs_validos = [
        "ALL",
        "SWRC_CATALOG",
        "JANG_ET_AL_CATALOG"
    ]

    if catalog not in catalogs_validos:
        return False

    return True

def donki_flr_validate_interval(start_date: str, end_date: str):
    
    if not start_date:
        start_date = (date.today() - timedelta(days=30)).strftime("%Y-%m-%d")

    if not end_date:
        end_date = date.today().strftime("%Y-%m-%d")

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

    return True
    
def donki_sep_validate_interval(start_date: str, end_date: str):
    
    if not start_date:
        start_date = (date.today() - timedelta(days=30)).strftime("%Y-%m-%d")

    if not end_date:
        end_date = date.today().strftime("%Y-%m-%d")

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

    return True

def donki_mpc_validate_interval(start_date: str, end_date: str):
    
    if not start_date:
        start_date = (date.today() - timedelta(days=30)).strftime("%Y-%m-%d")

    if not end_date:
        end_date = date.today().strftime("%Y-%m-%d")

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

    return True

def donki_rbe_validate_interval(start_date: str, end_date: str):
    
    if not start_date:
        start_date = (date.today() - timedelta(days=30)).strftime("%Y-%m-%d")

    if not end_date:
        end_date = date.today().strftime("%Y-%m-%d")

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

    return True

def donki_hss_validate_interval(start_date: str, end_date: str):
    
    if not start_date:
        start_date = (date.today() - timedelta(days=30)).strftime("%Y-%m-%d")

    if not end_date:
        end_date = date.today().strftime("%Y-%m-%d")

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

    return True

def donki_wsaenlilsimulation_validate_interval(start_date: str, end_date: str):
    
    if not start_date:
        start_date = (
            date.today() - timedelta(days=7)
        ).strftime("%Y-%m-%d")

    if not end_date:
        end_date = date.today().strftime("%Y-%m-%d")

    try:
        start_date_received = datetime.strptime(
            start_date, "%Y-%m-%d"
        ).date()

        end_date_received = datetime.strptime(
            end_date, "%Y-%m-%d"
        ).date()

    except ValueError:
        
        return False

    if start_date_received > date.today():
        return False

    if end_date_received > date.today():
        return False

    if start_date_received > end_date_received:
        return False
    
    return True

def donki_notification_validate_interval(start_date: str, end_date: str, type: str):
    
    if not start_date:
        start_date = (
            date.today() - timedelta(days=7)
        ).strftime("%Y-%m-%d")

    if not end_date:
        end_date = date.today().strftime("%Y-%m-%d")

    try:
        start_date_received = datetime.strptime(
            start_date, "%Y-%m-%d"
        ).date()

        end_date_received = datetime.strptime(
            end_date, "%Y-%m-%d"
        ).date()

    except ValueError:
        return False

    if start_date_received > date.today():
        return False

    if end_date_received > date.today():
        return False

    if start_date_received > end_date_received:
        return False

    if (end_date_received - start_date_received).days > 30:
        return False

    if not type:
        type = "all"

    tipos_validos = [
        "all",
        "FLR",
        "SEP",
        "CME",
        "IPS",
        "MPC",
        "GST",
        "RBE",
        "report"
    ]

    if type not in tipos_validos:
        return False

    return True

#----------------------------------------------------------------------------------------------------------------------------

def donki_cme_search_interval(start_date: str, end_date: str):
    if not donki_cme_validate_interval(start_date, end_date):
        return {"error": "Intervalo de datas inválido"}

    return nasa_rest_donki.donki_cme_search_nasa_cme(start_date, end_date)

def donki_cme_analysis_search(start_date: str, end_date: str, most_accurate_only: bool, complete_entry_only: bool, speed: int, half_angle: int, catalog: str, keyword: str):
    if not donki_cme_analysis_validate(start_date, end_date, most_accurate_only, complete_entry_only, speed, half_angle, catalog, keyword):
        return {"error": "Parâmetros de busca inválidos"}

    return nasa_rest_donki.donki_cme_analysis_search_nasa_cme_analysis(start_date, end_date, most_accurate_only, complete_entry_only, speed, half_angle, catalog, keyword)

def donki_gst_search_interval(start_date: str, end_date: str):
    if not donki_gst_validate_interval(start_date, end_date):
        return {"error": "Intervalo de datas inválido"}

    return nasa_rest_donki.donki_gst_search_nasa_gst(start_date, end_date)

def donki_ips_search_interval(start_date: str, end_date: str, location: str, catalog: str):
    if not donki_ips_validate_interval(start_date, end_date, location, catalog):
        return {"error": "Parâmetros de busca inválidos"}

    return nasa_rest_donki.donki_ips_search_nasa_ips(start_date, end_date, location, catalog)

def donki_flr_search_interval(start_date: str, end_date: str):
    if not donki_flr_validate_interval(start_date, end_date):
        return {"error": "Intervalo de datas inválido"}

    return nasa_rest_donki.donki_flr_search_nasa_flr(start_date, end_date)

def donki_sep_search_interval(start_date: str, end_date: str):
    if not donki_sep_validate_interval(start_date, end_date):
        return {"error": "Intervalo de datas inválido"}

    return nasa_rest_donki.donki_sep_search_nasa_sep(start_date, end_date)

def donki_mpc_search_interval(start_date: str, end_date: str):
    if not donki_mpc_validate_interval(start_date, end_date):
        return {"error": "Intervalo de datas inválido"}

    return nasa_rest_donki.donki_mpc_search_nasa_mpc(start_date, end_date)

def donki_rbe_search_interval(start_date: str, end_date: str):
    if not donki_rbe_validate_interval(start_date, end_date):
        return {"error": "Intervalo de datas inválido"}

    return nasa_rest_donki.donki_rbe_search_nasa_rbe(start_date, end_date)

def donki_hss_search_interval(start_date: str, end_date: str):
    if not donki_hss_validate_interval(start_date, end_date):
        return {"error": "Intervalo de datas inválido"}

    return nasa_rest_donki.donki_hss_search_nasa_hss(start_date, end_date)

def donki_wsaenlilsimulation_search_interval(start_date: str, end_date: str):
    if not donki_wsaenlilsimulation_validate_interval(start_date, end_date):
        return {"error": "Intervalo de datas inválido"}

    return nasa_rest_donki.donki_wsaenlilsimulation_search_nasa_wsaenlilsimulation(start_date, end_date),

def donki_notification_search_interval(start_date: str, end_date: str, type: str):
    if not donki_notification_validate_interval(start_date, end_date, type):
        return {"error": "Parâmetros de busca inválidos"}

    return nasa_rest_donki.donki_notification_search_nasa_notification(start_date, end_date, type)
