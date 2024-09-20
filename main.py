# Import necessary types and modules
from typing import Union  # Union is used for type hinting optional parameters
import random  # Used to generate a random light score

from fastapi import FastAPI  # FastAPI framework to create the API
from fastapi.middleware.cors import CORSMiddleware  # Middleware to handle CORS (Cross-Origin Resource Sharing)

# Initialize the FastAPI app
app = FastAPI()

# List of allowed origins for CORS (e.g., frontend URL for development)
origins = [
    "http://localhost:5173",  # Add other origins as needed for production or additional environments
]

import requests  # Import requests module for making HTTP requests (e.g., to external APIs)

# Add CORS middleware to allow cross-origin requests from the specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow requests from the specified origins
    allow_credentials=True,  # Allow credentials (cookies, authorization headers)
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all HTTP headers
)

# Default root endpoint, returns a simple JSON response
@app.get("/")
def read_root():
    return {
        "country": country,
        "city": city,
        "postal_code": postal_code,
        "street_number": street_number,
        "floor": floor,
        "light_score": light_score,
    }


# Endpoint to get an item by ID, with an optional query parameter (q)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    # Return the item_id and the optional query parameter
    return {"item_id": item_id, "q": q}

# Function to geocode an address using the Google Geocoding API
def geocode_address(address):
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key for Google Geocoding API
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address}&key={api_key}"
    response = requests.get(endpoint)  # Make a GET request to the Google Geocoding API
    if response.status_code == 200:  # Check if the request was successful
        results = response.json()['results']  # Parse the JSON response
        if results:
            # Extract latitude and longitude from the first result
            location = results[0]['geometry']['location']
            return location['lat'], location['lng']
    return None, None  # Return None if the address could not be geocoded

# Endpoint to get a random light score based on provided address details
@app.get("/light_score/")
def get_light_score(
    country: str,  # Country parameter (required)
    city: str,  # City parameter (required)
    postal_code: str,  # Postal code parameter (required)
    street_number: str,  # Street number parameter (required)
    floor: Union[str, None] = None  # Optional floor parameter (can be None)
):
    # Generate a random light score between 0 and 100
    light_score = random.randint(0, 100)
    
    # Return the provided address details along with the generated light score
    return {
        "country": country,
        "city": city,
        "postal_code": postal_code,
        "street_number": street_number,
        "floor": floor,
        "light_score": light_score,
    }
