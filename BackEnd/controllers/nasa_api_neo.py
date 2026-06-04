from fastapi import APIRouter
import BackEnd.services.nasa_service_neo as nasa_service_neo


router = APIRouter(prefix="/nasa")

@router.get("/neo/feed")
def search_neo_feed(start_date: str, end_date: str):
    return nasa_service_neo.neo_feed_search_interval(start_date, end_date)

@router.get("/neo/lookup/{asteroid_id}")
def search_neo_lookup(asteroid_id: int):
    return nasa_service_neo.neo_lookup_search(asteroid_id)

@router.get("/neo/browse")
def browse_neo():
    return nasa_service_neo.neo_browse_search()