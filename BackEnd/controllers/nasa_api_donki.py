from fastapi import APIRouter
import BackEnd.services.nasa_service_donki as nasa_service_donki


router = APIRouter(prefix="/nasa")

@router.get("/donki/cme")
def search_donki_cme(start_date: str = None, end_date: str = None):
    return nasa_service_donki.donki_cme_search_interval(start_date, end_date)

@router.get("/donki/cmeanalysis")
def search_donki_cme_analysis(start_date: str = None, end_date: str = None, most_accurate_only: bool = None, complete_entry_only: bool = None, speed: int = None, half_angle: int = None, catalog: str = None, keyword: str = None):
    return nasa_service_donki.donki_cme_analysis_search(start_date, end_date, most_accurate_only, complete_entry_only, speed, half_angle, catalog, keyword)

@router.get("/donki/gst")
def search_donki_gst(start_date: str = None, end_date: str = None):
    return nasa_service_donki.donki_gst_search_interval(start_date, end_date)

@router.get("/donki/ips")
def search_donki_ips(start_date: str = None, end_date: str = None,location: str = None, catalog: str = None):
    return nasa_service_donki.donki_ips_search_interval(start_date, end_date,location,catalog)

@router.get("/donki/flr")
def search_donki_flr(start_date: str = None, end_date: str = None):
    return nasa_service_donki.donki_flr_search_interval(start_date, end_date)

@router.get("/donki/sep")
def search_donki_sep(start_date: str = None, end_date: str = None):
    return nasa_service_donki.donki_sep_search_interval(start_date, end_date)

@router.get("/donki/mpc")
def search_donki_mpc(start_date: str = None, end_date: str = None):
    return nasa_service_donki.donki_mpc_search_interval(start_date, end_date)

@router.get("/donki/rbe")
def search_donki_rbe(start_date: str = None, end_date: str = None):
    return nasa_service_donki.donki_rbe_search_interval(start_date, end_date)

@router.get("/donki/hss")
def search_donki_hss(start_date: str = None, end_date: str = None):
    return nasa_service_donki.donki_hss_search_interval(start_date, end_date)

@router.get("/donki/wsaenlilsimulation")
def search_donki_wsaenlilsimulation(start_date: str = None, end_date: str = None):
    return nasa_service_donki.donki_wsaenlilsimulation_search_interval(start_date, end_date)

@router.get("/donki/notifications")
def search_donki_notification(start_date: str = None, end_date: str = None,type: str = None):
    return nasa_service_donki.donki_notification_search_interval(start_date, end_date,type)