from fastapi import APIRouter

import services.nasa_service as nasa_service 

router = APIRouter(prefix="/nasa")


@router.get("/apod/fotos")
def search_photo(date: str):
    return nasa_service.search_photo(date)

@router.get("/asteroides/objetos")
def search_asteroids(start_date: str, end_date: str):
    return nasa_service.search_asteroids(start_date, end_date)