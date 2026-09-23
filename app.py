# FastAPI creates the server and the exceptions 
from fastapi import FastAPI, HTTPException

# Import the graph implementation that calculates the path from USA.
from find_path import Node

app = FastAPI()

@app.get("/{country}")
def get_path(country: str):
    # FastAPI reads the country code from a URL such as /PAN.
    path = Node("USA").find_path(country)

    # Return error when the country code is invalid.
    if isinstance(path, str):
        raise HTTPException(status_code=400, detail=path)

    # Return the destination and shortest path as JSON.
    return {
        "destination": country.upper(),
        "list": path,
    }
