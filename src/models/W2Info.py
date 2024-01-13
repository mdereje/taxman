from typing import List
from decimal import Decimal
from pydantic import BaseModel

class W2Info(BaseModel):
    wages: Decimal
    federal_income_tax_withheld: Decimal
    social_security_tax_withheld: Decimal
    state_income_taxes: List[dict]
    
    def __init__(self, wages: Decimal, federal_income_tax_withheld: Decimal, social_security_tax_withheld: Decimal, state_income_taxes: List[dict]):
        self.wages = wages
        self.federal_income_tax_withheld = federal_income_tax_withheld
        self.social_security_tax_withheld = social_security_tax_withheld
        self.state_income_taxes = state_income_taxes

    def to_dict(self):
        return {
            'wages': str(self.wages),
            'federal_income_tax_withheld': str(self.federal_income_tax_withheld),
            'social_security_tax_withheld': str(self.social_security_tax_withheld),
            'state_income_taxes': self.state_income_taxes
        }