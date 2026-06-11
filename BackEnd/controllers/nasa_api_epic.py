from fastapi import APIRouter
import BackEnd.services.nasa_service_epic as nasa_service_epic


router = APIRouter(prefix="/nasa")

@router.get("/epic/natural")
def search_epic():
    return nasa_service_epic.epic_search()

@router.get("/epic/natural/date/{date}")
def search_epic_by_date(date: str):
    return nasa_service_epic.epic_search_by_date(date)

@router.get("/epic/natural/all/")
def search_epic_all():
    return nasa_service_epic.epic_search_all()

@router.get("/epic/natural/available")
def search_epic_available():
    return nasa_service_epic.epic_search_available()

@router.get("/epic/enhanced")
def search_epic_enhanced():
    return nasa_service_epic.epic_search_enhanced()

@router.get("/epic/enhanced/date/{date}")
def search_epic_enhanced_by_date(date: str):
    return nasa_service_epic.epic_search_enhanced_by_date(date) 

@router.get("/epic/enhanced/all/")
def search_epic_enhanced_all():
    return nasa_service_epic.epic_search_enhanced_all()

@router.get("/epic/enhanced/available")
def search_epic_enhanced_available():    
    return nasa_service_epic.epic_search_enhanced_available()

@router.get("/epic/aerosol")
def search_epic_aerosol():
    return nasa_service_epic.epic_search_aerosol()

@router.get("/epic/aerosol/date/{date}")
def search_epic_aerosol_by_date(date: str):
    return nasa_service_epic.epic_search_aerosol_by_date(date) 

@router.get("/epic/aerosol/all/")
def search_epic_aerosol_all():  
    return nasa_service_epic.epic_search_aerosol_all()

@router.get("/epic/aerosol/available")
def search_epic_aerosol_available():
    return nasa_service_epic.epic_search_aerosol_available()

@router.get("/epic/cloud")
def search_epic_cloud():
    return nasa_service_epic.epic_search_cloud()    

@router.get("/epic/cloud/date/{date}")
def search_epic_cloud_by_date(date: str):
    return nasa_service_epic.epic_search_cloud_by_date(date)    

@router.get("/epic/cloud/all/")
def search_epic_cloud_all():
    return nasa_service_epic.epic_search_cloud_all()    

@router.get("/epic/cloud/available")
def search_epic_cloud_available():
    return nasa_service_epic.epic_search_cloud_available()