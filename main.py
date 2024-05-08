from fastapi import FastAPI
from fastapi.responses import FileResponse

import requests

app = FastAPI()
favicon_path = "favicon.ico"


casualties_url = "https://data.techforpalestine.org/api/v2/casualties_daily.min.json"
killed_url = "https://data.techforpalestine.org/api/v2/killed-in-gaza.min.json"
westbank_url = "https://data.techforpalestine.org/api/v2/west_bank_daily.min.json"

casualties_csv = requests.get(casualties_url).json()
killed_csv = requests.get(killed_url).json()
westbank_csv = requests.get(westbank_url).json()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/killed")
async def killed(limit: int | None = None):
    return killed_csv[0:limit]


@app.get("/casualties")
async def casualties(limit: int | None = None):
    return casualties_csv[0:limit]


@app.get("/westbank")
async def westbank(limit: int | None = None):
    return westbank_csv[0:limit]


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)
