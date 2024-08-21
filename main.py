from typing import Union
import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:5173",  # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/light_score/")
def get_light_score(
    country: str,
    city: str,
    postal_code: str,
    street_number: str,
    floor: Union[str, None] = None
):
    # Generate a random score between 0 and 100
    light_score = random.randint(0, 100)
    return {
        "country": country,
        "city": city,
        "postal_code": postal_code,
        "street_number": street_number,
        "floor": floor,
        "light_score": light_score
    }