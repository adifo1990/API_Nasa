from datetime import date, datetime, timedelta

from BackEnd.rest import nasa_rest_epic

def epic_natural_validate_date(date_str: str):

    if not date_str:
        return False

    try:
        date_received = datetime.strptime(
            date_str,
            "%Y-%m-%d"
        ).date()

    except ValueError:
        return False

    min_date = date(2015, 6, 13)

    if date_received < min_date:
        return False

    if date_received > date.today():
        return False

    return True
    
def epic_enhanced_validate_date(date_str: str):

    if not date_str:
        return False

    try:
        date_received = datetime.strptime(
            date_str,
            "%Y-%m-%d"
        ).date()

    except ValueError:
        return False

    min_date = date(2015, 6, 17)

    if date_received < min_date:
        return False

    if date_received > date.today():
        return False

    return True

def epic_aerosol_validate_date(date_str: str):

    if not date_str:
        return False

    try:
        date_received = datetime.strptime(
            date_str,
            "%Y-%m-%d"
        ).date()

    except ValueError:
        return False

    min_date = date(2015, 6, 17)

    if date_received < min_date:
        return False

    if date_received > date.today():
        return False

    return True

def epic_cloud_validate_date(date_str: str):

    if not date_str:
        return False

    try:
        date_received = datetime.strptime(
            date_str,
            "%Y-%m-%d"
        ).date()

    except ValueError:
        return False

    min_date = date(2025, 7, 15)

    if date_received < min_date:
        return False

    if date_received > date.today():
        return False

    return True

#----------------------------------------------------------------------------------------------------------------------------

def epic_search():

    return nasa_rest_epic.epic_search_nasa_epic_natural()

def epic_search_by_date(date_str: str):

    if not epic_natural_validate_date(date_str):
        return {"error": "Data inválida"}

    return nasa_rest_epic.epic_search_nasa_epic_natural_by_date(date_str)

def epic_search_all():

    return nasa_rest_epic.epic_search_nasa_epic_natural_all()

def epic_search_available():

    return nasa_rest_epic.epic_search_nasa_epic_natural_available()

def epic_search_enhanced():

    return nasa_rest_epic.epic_search_nasa_epic_enhanced()

def epic_search_enhanced_by_date(date_str: str):

    if not epic_enhanced_validate_date(date_str):
        return {"error": "Data inválida"}

    return nasa_rest_epic.epic_search_nasa_epic_enhanced_by_date(date_str)

def epic_search_enhanced_all():

    return nasa_rest_epic.epic_search_nasa_epic_enhanced_all()

def epic_search_enhanced_available():

    return nasa_rest_epic.epic_search_nasa_epic_enhanced_available()

def epic_search_aerosol():

    return nasa_rest_epic.epic_search_nasa_epic_aerosol()

def epic_search_aerosol_by_date(date_str: str):

    if not epic_aerosol_validate_date(date_str):
        return {"error": "Data inválida"}

    return nasa_rest_epic.epic_search_nasa_epic_aerosol_by_date(date_str)

def epic_search_aerosol_all():

    return nasa_rest_epic.epic_search_nasa_epic_aerosol_all()   

def epic_search_aerosol_available():

    return nasa_rest_epic.epic_search_nasa_epic_aerosol_available()

def epic_search_cloud():

    return nasa_rest_epic.epic_search_nasa_epic_cloud()

def epic_search_cloud_by_date(date_str: str):  

    if not epic_cloud_validate_date(date_str):
        return {"error": "Data inválida"}

    return nasa_rest_epic.epic_search_nasa_epic_cloud_by_date(date_str)

def epic_search_cloud_all():

    return nasa_rest_epic.epic_search_nasa_epic_cloud_all()

def epic_search_cloud_available():

    return nasa_rest_epic.epic_search_nasa_epic_cloud_available()

