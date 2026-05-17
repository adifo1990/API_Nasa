from fastapi import APIRouter

import services.nasaService as nasa_service 

router = APIRouter(prefix="/nasa")


@router.get("/apod/fotos")
def buscar_foto(date: str):
    return nasa_service.buscar_foto(date)