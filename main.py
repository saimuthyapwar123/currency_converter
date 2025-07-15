from fastapi import FastAPI
from app.api.route import router as currency_router

app = FastAPI(title = "Currency Converter API")
app.include_router(currency_router, prefix="/currency")