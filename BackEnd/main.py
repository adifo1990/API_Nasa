from fastapi import FastAPI
from controllers.nasaAPI import router as nasa_router
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

app.include_router(nasa_router)

app.mount("/css", StaticFiles(directory="../FrontEnd/css"), name="css")
app.mount("/js", StaticFiles(directory="../FrontEnd/js"), name="js")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=3000,
        reload=True
    )


@app.get("/")
def home():
    return FileResponse("../FrontEnd/index.html")
