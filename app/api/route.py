from fastapi import APIRouter, HTTPException
from app.model.schemas import CurrencyRequest
from app.services.converter import convert
from app.utils.helper import save_conversion_record, get_logger,load_json_data


router = APIRouter()
logger = get_logger(__name__)

@router.post("/convert")
async def convet_currency(request:CurrencyRequest):
    try:
        result = await convert(request.amount, request.from_currency, request.to_currency)
        logger.info(f"Amount converted from ( {request.amount}.{request.from_currency.upper()}) to ({result}.{request.to_currency.upper()})")
        save_conversion_record(request.amount, request.from_currency.upper(), request.to_currency.upper(), result)
        return {"message":f"Amount is successfully converted from ( {request.amount}.{request.from_currency.upper()}) to ({result}.{request.to_currency.upper()})"}
        
    except ValueError as ve :
        logger.error(str(ve))
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e :
        logger.exception("Unexpexted error")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/get_currencies")
def get_conversion_history():
    try:
        history =load_json_data()
        logger.info(f"All converted Currency are Loaded")
        return {"CONVERTED CURRENCY": history}
    except Exception as e:
        logger.exception("Failed to load Data")
        raise HTTPException(status_code=500, detail="Failed to load Data")