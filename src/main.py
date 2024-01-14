from rich.console import Console
from src.integrations.fiscalData import FiscalDataService
from src.models.W2Info import W2Info
from fastapi import FastAPI
from decimal import Decimal
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

console = Console()
fiscalDataService = FiscalDataService()
result = fiscalDataService.getExchangeRates()
listOfResults = list(result['data'])
print(len(listOfResults))


app = FastAPI()

@app.get("/health")
def hello():
  return {'API Status': 'Healthy'} 


'''
curl -X POST -H "Content-Type: application/json" -d '{
    "wages": 5000,
    "federal_income_tax_withheld": 1000,
    "social_security_tax_withheld": 200,
    "state_income_taxes": [
        {
            "state": "CA",
            "incomeTaxPayed": 200
        }
    ]
}' http://localhost:8000/w2Info
'''
@app.post("/w2Info")
def calculateTaxes(w2Info: W2Info) -> str:
    try:
        print(w2Info)
        console.print(f"[u][bold cyan]{w2Info}[/bold cyan][/u]",justify="center")
        return JSONResponse(content=jsonable_encoder(w2Info), status_code=200)
    except AttributeError as e:
        print(e)
        return str(e)
