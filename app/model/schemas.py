from pydantic import BaseModel

class CurrencyRequest(BaseModel):
    amount:float
    from_currency:str
    to_currency:str

class ConversionResponse(BaseModel):
    amount:float
    from_currency:str
    to_currency:str
    converted_amount:float