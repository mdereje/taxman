import requests
from rich.console import Console

req = requests.request('GET', 'https://httpbin.org/get')

console = Console()
console.print(f"[u][bold cyan]{req.content}[/bold cyan][/u]",justify="center")

# Input model being set with a w2.
w2Info = {
    "wages": 140406.79,
    "federalIncomeTaxWitheld": 24125.21,
    "socialSecurityWages": 145225.80,
    "socialSecurityTaxWitheld": 9004.00,
    "stateInfo":[
        {
            "wages": 2539.87,
            "state": "CA",
            "incomeTaxPayed": 114.10,
        },
        {
            "wages": 137866.92,
            "state": "MA",
            "incomeTaxPayed": 6502.25,
        }
    ]
}

# 