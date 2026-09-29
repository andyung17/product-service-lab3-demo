import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# load environment
load_dotenv()
port_env = os.getenv("PORT", "3030")

# setting port
try:
    port = int(port_env)
except ValueError:
    raise ValueError("Invalid PORT")

# initalize FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get endpoint
@app.get("/products")
async def get_products():
    return [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)