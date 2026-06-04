from fastapi import APIRouter
import BackEnd.services.nasa_service_apod as nasa_service_apod


router = APIRouter(prefix="/nasa")

@router.get("/apod/photo")
def search_apod_photo(date: str):
    return nasa_service_apod.apod_search_photo(date)

@router.get("/apod/photos")
def search_apod_photos_interval(start_date: str, end_date: str):
    return nasa_service_apod.apod_search_photos_interval(start_date, end_date)

@router.get("/apod/photos/count")
def search_apod_photos_count(count: int):
    return nasa_service_apod.apod_search_photos_count(count)

@router.get("/apod/photos/thumbs")
def search_apod_photos_thumbs(thumbs: bool):
    return nasa_service_apod.apod_search_photos_thumbs(thumbs)