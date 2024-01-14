import json
from rich.console import Console
from src.integrations.fiscalData import FiscalDataService
from src.models.W2Info import W2Info

from fastapi import FastAPI
from decimal import Decimal

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
        info = W2Info(Decimal('5000'), Decimal('1000'), Decimal('500'), [{'state': 'CA', 'value': Decimal('200')}])
        json_info = json.dumps(info.to_dict())
        return json_info
    except AttributeError as e:
        print(e)
        return str(e)
