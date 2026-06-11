from fastapi import APIRouter
import BackEnd.services.nasa_service_insight as nasa_service_insight


router = APIRouter(prefix="/nasa")

@router.get("/insight")
def search_insight():
    return nasa_service_insight.insight_search()
