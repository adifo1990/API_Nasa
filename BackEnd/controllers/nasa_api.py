from fastapi import APIRouter
import services.nasa_service as nasa_service


router = APIRouter(prefix="/nasa")

@router.get("/apod/photo")
def search_apod_photo(date: str):
    return nasa_service.apod_search_photo(date)

@router.get("/apod/photos")
def search_apod_photos_interval(start_date: str, end_date: str):
    print("Datas recebidas busca intervalo:", start_date, end_date)
    return nasa_service.apod_search_photos_interval(start_date, end_date)

@router.get("/apod/photos/count")
def search_apod_photos_count(count: int):
    return nasa_service.apod_search_photos_count(count)

@router.get("/apod/photos/thumbs")
def search_apod_photos_thumbs(thumbs: bool):
    return nasa_service.apod_search_photos_thumbs(thumbs)

@router.get("/neo/feed")
def search_neo_feed(start_date: str, end_date: str):
    print("Datas recebidas buscar_asteroides_donki:", start_date, end_date)
    return nasa_service.neo_feed_search_interval(start_date, end_date)