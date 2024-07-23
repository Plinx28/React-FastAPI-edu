from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.router import router as router_cmc

app = FastAPI(title="Cryptocurrencies with React")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://89.223.126.16"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=("GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"),
    allow_headers=("Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"),
)

app.include_router(router_cmc)




