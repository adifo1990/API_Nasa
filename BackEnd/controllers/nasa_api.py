from fastapi import APIRouter

import services.nasa_service as nasa_service 

router = APIRouter(prefix="/nasa")


@router.get("/apod/photo")
def search_photo(date: str):
    return nasa_service.search_photo(date)

@router.get("/photos/interval")
def search_photos_interval(start_date: str, end_date: str, search_mode: str):
    print("Datas recebidas busca intervalo:", start_date, end_date, search_mode)
    return nasa_service.search_photos_interval(start_date, end_date, search_mode)

@router.get("/apod/photos/count")
def search_photos_count(count: int):
    return nasa_service.search_photos_count(count)

@router.get("/apod/photos/thumbs")
def search_photos_thumbs(thumbs: bool):
    return nasa_service.search_photos_thumbs(thumbs)