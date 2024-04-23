from fastapi import FastAPI
import requests

app = FastAPI()

casualties_url = "https://raw.githubusercontent.com/TechForPalestine/palestine-datasets/b0328917f163c55fb03de6184395bafdd22b35ec/casualties_daily.min.json"
killed_url = "https://raw.githubusercontent.com/TechForPalestine/palestine-datasets/b0328917f163c55fb03de6184395bafdd22b35ec/killed-in-gaza.min.json"
westbank_url = "https://raw.githubusercontent.com/TechForPalestine/palestine-datasets/b0328917f163c55fb03de6184395bafdd22b35ec/west_bank_daily.min.json"

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
