import requests

# List of endpoints can be found here https://fiscaldata.treasury.gov/api-documentation/#list-of-endpoints
class FiscalDataService:

    
    def __init__(self) -> None:
        self.baseURL = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
        self.endpoints = {
            "exchange-rate": "/v1/accounting/od/rates_of_exchange"
        }
        
    def getExchangeRates(self, recordDate:str = '2023-01-01', currencyFilter= ['Canada-Dollar','Mexico-Peso'], fields=['country_currency_desc','exchange_rate','record_date'], dateCompare='eq'):
        '''
        record_date = YYYY-MM-dd
        fields = country_currency_desc, exchange_rate,record_dat
        filter=country_currency_desc:in:(Canada-Dollar,Mexico-Peso)
        dateCompare =   lt= Less than
                    lte= Less than or equal to
                    gt= Greater than
                    gte= Greater than or equal to
                    eq= Equal to
                    in= Contained in a given set
        '''
        currencies = f""
        
            
        params = f"?fields={','.join(fields)}&filter="
        
        if currencyFilter:
            params += f"country_currency_desc:in:({','.join(currencyFilter)})"
        if dateCompare:
            params += f',{dateCompare}:{recordDate}'
        
        r = requests.get(f"{self.baseURL}{self.endpoints['exchange-rate']}{params}")
        return r.json()
        