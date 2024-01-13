# import requests
import json
from rich.console import Console
from integrations.fiscalData import FiscalDataService
from models.W2Info import W2Info

# req = requests.request('GET', 'https://httpbin.org/get')

# console = Console()
# console.print(f"[u][bold cyan]{req.content}[/bold cyan][/u]",justify="center")

# Input model being set with a w2.
# w2Info = {
#     "wages": 140406.79,
#     "federalIncomeTaxWitheld": 24125.21,
#     "socialSecurityWages": 145225.80,
#     "socialSecurityTaxWitheld": 9004.00,
#     "stateInfo":[
#         {
#             "wages": 2539.87,
#             "state": "CA",
#             "incomeTaxPayed": 114.10,
#         },
#         {
#             "wages": 137866.92,
#             "state": "MA",
#             "incomeTaxPayed": 6502.25,
#         }
#     ]
# }


# fiscalDataService = FiscalDataService()
# result = fiscalDataService.getExchangeRates()
# listOfResults = list(result['data'])
# print(len(listOfResults))

from fastapi import FastAPI
from decimal import Decimal

app = FastAPI()

@app.get("/health")
def hello():
  return {'API Status': 'Healthy'} 


'''
curl -X POST -H "Content-Type: application/json" -d '{
    "wages": 5000,
    "federalIncomeTaxWitheld": 1000,
    "socialSecurityTaxWitheld": 200,
    "stateInfo": [
        {
            "state": "CA",
            "incomeTaxPayed": 200
        }
    ]
}' http://localhost:8000/w2Info
'''
@app.post("/w2Info")
def calculateTaxes(w2Info: W2Info) -> str:
    print(w2Info)
    info = W2Info(['CA', 'NY'], Decimal('5000'), Decimal('1000'), Decimal('500'), [{'state': 'CA', 'value': Decimal('200')}])
    json_info = json.dumps(info.to_dict())
    return json_info
