from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = [
    "http://localhost:3000/",
    "*"
]

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
    headers = {"x-apikey": "bfa467937a1d01a44c02e741b74d9760618fa151b4071f756b1bd57547b81565",
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
