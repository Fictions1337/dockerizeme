from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/message")
def get_message():
    url = "http://91.99.128.94:9000/helper"
    response = requests.get(url)
    helper_message = response.json()["helper_message"]

    return {
        "message": f"Backend received: {helper_message}"
    }
