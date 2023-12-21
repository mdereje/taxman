import requests

# List of endpoints can be found here https://fiscaldata.treasury.gov/api-documentation/#list-of-endpoints
class FiscalDataService:

    
    def __init__(self) -> None:
        self.baseURL = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
        self.endpoints = {
            "exchange-rate": "/v1/accounting/od/rates_of_exchange"
        }
        
    def getExchangeRates(self, recordDate:str = '2023-01-01', currencyFilter= ['Canada-Dollar','Mexico-Peso'], fields=['country_currency_desc','exchange_rate','record_date'], dateCompare='eq'):
        """Get exchange rates!

        Args:
            recordDate (str, optional): _description_. Defaults to '2023-01-01'.
            currencyFilter (list, optional): _description_. Defaults to ['Canada-Dollar','Mexico-Peso'].
            fields (list, optional): _description_. Defaults to ['country_currency_desc','exchange_rate','record_date'].
            dateCompare (str, optional): _description_. Defaults to 'eq'.

        Returns:
            _type_: _description_
        """
        currencies = f""
        
            
        params = f"?fields={','.join(fields)}&filter="
        
        if currencyFilter:
            params += f"country_currency_desc:in:({','.join(currencyFilter)})"
        if dateCompare:
            params += f',{dateCompare}:{recordDate}'
        
        r = requests.get(f"{self.baseURL}{self.endpoints['exchange-rate']}{params}")
        return r.json()
        