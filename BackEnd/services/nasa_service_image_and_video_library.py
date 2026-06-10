from datetime import datetime

import BackEnd.rest.nasa_rest_image_and_video_library as nasa_rest_image_and_video_library

def image_and_video_library_validate(q: str, center: str = None, description: str = None, description_508: str = None,
                                   keywords: str = None, location: str = None, media_type: str = None, nasa_id: str = None,
                                   page: int = None, page_size: int = None, photographer: str = None,
                                   secondary_creator: str = None, title: str = None, year_start: str = None, year_end: str = None):

    if not q:
        print("Informe o parâmetro q")
        return False

    if page is not None:
        if not isinstance(page, int) or page < 1:
            print("page deve ser um inteiro maior que 0")
            return False

    if page_size is not None:
        if not isinstance(page_size, int) or page_size < 1:
            print("page_size deve ser um inteiro maior que 0")
            return False

    if year_start:
        try:
            datetime.strptime(year_start, "%Y")
        except ValueError:
            print("year_start deve estar no formato YYYY")
            return False

    if year_end:
        try:
            datetime.strptime(year_end, "%Y")
        except ValueError:
            print("year_end deve estar no formato YYYY")
            return False

    if year_start and year_end:
        if int(year_start) > int(year_end):
            print("year_start não pode ser maior que year_end")
            return False

    return True

#----------------------------------------------------------------------------------------------------------------------------

def image_and_video_library_search(q: str, center: str = None, description: str = None, description_508: str = None,
                                   keywords: str = None, location: str = None, media_type: str = None, nasa_id: str = None,
                                   page: int = None, page_size: int = None, photographer: str = None,
                                   secondary_creator: str = None, title: str = None, year_start: str = None, year_end: str = None):

    if not image_and_video_library_validate(q, center, description, description_508, keywords, location, media_type, nasa_id, page, page_size, photographer, secondary_creator, title, year_start, year_end):
        return {"error": "Parâmetros inválidos"}

    return nasa_rest_image_and_video_library.image_and_video_library_search(q, center, description, description_508, keywords, location, media_type, nasa_id, page, page_size, photographer, secondary_creator, title, year_start, year_end)    