from datetime import date, datetime

from BackEnd.rest import nasa_rest_insight

def insight_search():

    return nasa_rest_insight.insight_search_nasa_insight()

