from fastapi import FastAPI
from BackEnd.controllers.nasa_api_apod import router as nasa_router_apod
from BackEnd.controllers.nasa_api_neo import router as nasa_router_neo
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import uvicorn

app = FastAPI()

origins = [
    "http://localhost:3000",
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

app.mount("/css", StaticFiles(directory="FrontEnd/css"), name="css")
app.mount("/js", StaticFiles(directory="FrontEnd/js"), name="js")
app.mount("/pages", StaticFiles(directory="FrontEnd/pages"), name="pages")

if __name__ == "__main__":
    uvicorn.run(
        "BackEnd.main:app",
        host="localhost",
        port=3000,
        reload=True
    )

@app.get("/")
def home():
    return FileResponse("../FrontEnd/index.html")
