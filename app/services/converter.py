from app.config.country_code_rates import EXCHANGE_RATES

async def convert(amount:float, from_currency:str, to_currency:str) -> float:
    from_currency= from_currency.upper()
    to_currency= to_currency.upper()

    if from_currency not in EXCHANGE_RATES:
        raise ValueError(f"Unsupported Currency:{from_currency}")
    
    if to_currency not in EXCHANGE_RATES:
        raise ValueError(f"Unsupported Currency:{to_currency}")
    
    requested_amount = amount/EXCHANGE_RATES[from_currency]
    return round((requested_amount*EXCHANGE_RATES[to_currency]), 2)
    
    

