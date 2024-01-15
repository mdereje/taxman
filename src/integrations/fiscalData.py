import requests
from src.util.logger import Logger
import urllib

# List of endpoints can be found here https://fiscaldata.treasury.gov/api-documentation/#list-of-endpoints
class FiscalDataService:

    
    def __init__(self) -> None:
        self.logger = Logger(logger_name="FiscalDataService")
        self.baseURL = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
        self.endpoints = {
            "exchange-rate": "/v1/accounting/od/rates_of_exchange",
            "revenue-collections":"/v2/revenue/rcm"
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
            
        params = f"?fields={','.join(fields)}&filter="
        
        if currencyFilter:
            params += f"country_currency_desc:in:({','.join(currencyFilter)})"
        if dateCompare:
            params += f',{dateCompare}:{recordDate}'
        
        r = requests.get(f"{self.baseURL}{self.endpoints['exchange-rate']}{params}")
        return r.json()
        
    def getUsGovernementCollections(self, filter_start_date:str='2023-01-01', filter_end_date:str = '2023-12-31', tax_category_desc='IRS Tax') -> str:
        # 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/revenue/rcm?filter=record_date:gte:2023-01-01,record_date:lte:2023-12-31,tax_category_desc:eq:IRS%20Tax'
        # 'https://api.fiscaldata.treasury.gov/services/api/fiscal_servicev2/revenue/rcm?filter=record_date:gte2023-01-01,record_date:lte:2023-12-31,tax_category_desc:eq:IRS'
        """
        The U.S. Government Revenue Collections dataset provides a daily overview of federal revenue collections such as individual and corporate income tax deposits, customs duties, fees for government service, fines, and loan repayments. These collections can be made through either electronic or non-electronic transactions by mail, internet, bank, or over-the-counter channels.
        Returns:
            str: The US government collections data.
        """
        try:
            fields = ['record_date','electronic_category_desc','channel_type_desc','tax_category_desc','net_collections_amt']
            params = f"?filter=record_date:gte:{filter_start_date},record_date:lte:{filter_end_date},tax_category_desc:eq:{urllib.parse.quote_plus(tax_category_desc)}"
            fullURL = f"{self.baseURL}{self.endpoints['revenue-collections']}{params}&fields={','.join(fields)}"
            
            r = requests.get(fullURL)
            self.logger.info(f"Making request to {fullURL}")
            return r.json()
        except requests.exceptions.RequestException as e:
            # Handle exception here
            self.logger.error(f"Error making request to {fullURL} {e}")
            return None
