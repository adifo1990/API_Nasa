from fastapi import APIRouter
import BackEnd.services.nasa_service_donki as nasa_service_donki


router = APIRouter(prefix="/nasa")

@router.get("/donki/cme")
def search_donki_cme(start_date: str, end_date: str):
    print("Datas recebidas donki cme:", start_date, end_date)
    return nasa_service_donki.donki_cme_search_interval(start_date, end_date)