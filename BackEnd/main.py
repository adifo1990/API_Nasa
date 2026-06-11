from fastapi import FastAPI
from BackEnd.controllers.nasa_api_apod import router as nasa_router_apod
from BackEnd.controllers.nasa_api_neo import router as nasa_router_neo
from BackEnd.controllers.nasa_api_donki import router as donki_router
from BackEnd.controllers.nasa_api_epic import router as epic_router
from BackEnd.controllers.nasa_api_insight import router as insight_router
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nasa_router_apod)
app.include_router(nasa_router_neo)
app.include_router(donki_router)
app.include_router(epic_router)
app.include_router(insight_router)




if __name__ == "__main__":
    uvicorn.run(
        "BackEnd.main:app",
        host="localhost",
        port=3000,
        reload=True
    )


