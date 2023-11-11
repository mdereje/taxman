## The idea
A user is able to put in their w2's for the year and the application should display show them exactly what they have payed for.
It should break down each income tax paid by:
- Federal
- State
- Local (if applicable)

## How do we make this?
How do we get government spending data for all the levels of government. We need to find all publicly available APIs and websites required for scraping.
We also need information on how income tax is broken down by state level vs federal level.

## Whats the idea place to start?
The first step would be to break down the federal income tax and how the government has spent the budget in the last fiscal year.
Then it would be to gather all the tax collected and spending by state.

## First step input output

**Input** :
- Total income for last year
Business info:
- Tax bracket for income
- Federal allocated budge for last year
- Federal spending for last year
- Federal elected officials
Output: 
- Break down of federal spending based on taxes paid/owed.

## Questions
- How does TurboTax get info about the tax payer by just using a W-2 number?
## APIs available

- [Fiscal Data](https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/deposits-and-withdrawals-of-operating-cash) for federal cash flow
- [Breakdown of federal spending](https://www.usaspending.gov/explorer/budget_function)
	- API version can be found [here](https://api.usaspending.gov/docs/endpoints) although i'm not sure how you can have sort of key. It says "endpoints do not currently require authorization."
	- [github read me](https://github.com/fedspendingtransparency/usaspending-api/blob/master/usaspending_api/api_contracts/contracts/v2/agency/toptier_code.md)

```Bash
curl -X GET https://api.usaspending.gov/api/v2/agency/012/
```
```JSON
{
  "fiscal_year": 2024,
  "toptier_code": "012",
  "name": "Department of Agriculture",
  "abbreviation": "USDA",
  "agency_id": 95,
  "icon_filename": "USDA.jpg",
  "mission": "We provide leadership on food, agriculture, natural resources, rural development, nutrition, and related issues based on sound public policy, the best available science, and efficient management.",
  "website": "https://www.usda.gov/",
  "congressional_justification_url": "https://www.usda.gov/cj",
  "about_agency_data": null,
  "subtier_agency_count": 27,
  "def_codes": [],
  "messages": []
}
```