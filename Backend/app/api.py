from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = [
    "http://localhost:3000/",
    "*"
]

API_KEY = "Your API Key"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/virustotal/{hash}")
async def virustotal(hash: str):
    url = f"https://www.virustotal.com/api/v3/files/{hash}"
    headers = {"x-apikey": API_KEY,
               "content-type": "text/plain"}
    response = requests.get(url, headers=headers)
    data = response.json()

    # Extract the relevant information from the response
    try:
        attributes = data["data"]["attributes"]
        summary = {
            "type": attributes["type"],
            "md5": attributes["md5"],
            "sha1": attributes["sha1"],
            "sha256": attributes["sha256"],
            "last_analysis_stats": attributes["last_analysis_stats"],
            "last_analysis_results": attributes["last_analysis_results"]
        }

        # Return the information in a JSON response
        return summary
    except:
        return data


@app.get("/")
async def root():
    return {"message": "Hello World"}
