from fastapi import APIRouter
import BackEnd.services.nasa_service_image_and_video_library as nasa_service_image_and_video_library


router = APIRouter(prefix="/nasa")

@router.get("/image_and_video_library/search/q")
def search_image_and_video_library(q: str, center: str = None, description: str = None, description_508: str = None,
                                   keywords: str = None, location: str = None, media_type: str = None, nasa_id: str = None,
                                   page: int = None, page_size: int = None, photographer: str = None,
                                   secondary_creator: str = None, title: str = None, year_start: str = None, year_end: str = None):
    return nasa_service_image_and_video_library.image_and_video_library_search(q, center, description, description_508, keywords, location, media_type, nasa_id, page, page_size, photographer, secondary_creator, title, year_start, year_end)