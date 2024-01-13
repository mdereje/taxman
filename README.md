# TAXMAN
## TO Run
 - `cd src`
 - `python3 -m uvicorn main:app --reload`
 - go to http://127.0.0.1:8000/doc


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

Alright we are here but can we get in a better possession? So far it seems like it works and i like it but the keyboard alone is not enough

### Income tax data
https://taxfoundation.org/data/all/state/state-income-tax-rates-2023/
Income tax data has been downloaded from here.
If we cannot find something better, we can script this into a database and serve it as an API.
https://smartasset.com/taxes/massachusetts-tax-calculator#YdvuuRrYUt
There is also a calculator service. We can use that.

#### MA
```Shell
curl 'https://smartasset.com/taxes/massachusetts-tax-calculator?render=json&' \
  -H 'authority: smartasset.com' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'cookie: _sa_orig_ex=1cCoLzXyg9W6KHjLwbtF6nRKqUWjoSocz73UDMEEjBxtJhIl1qKJ8pIFvcYOjm6Q; _sa_lt=rgd1aKDxAhmKd7R5HTE5TwzkruZMCdJF; _sa_pt=ERmMUwpljmC6SPQBr4lZR9eHbqF2WHxtDW3TlkhuaTnu03mS2C4YVIAP9XCZT4D2; _sa_st_w_mortgagepurchaserates=mrg7FxPg7eR0BNWY4x7UevvI; landingPage=smartasset.com/taxes/massachusetts-tax-calculator; _sa_st=krRNmX5jC5ksPAn1ewojtHff' \
  -H 'origin: https://smartasset.com' \
  -H 'pragma: no-cache' \
  -H 'referer: https://smartasset.com/taxes/massachusetts-tax-calculator' \
  -H 'sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest' \
  --data-raw 'ud-it-household-income=137867' \
  --compressed
```

#### CA
```Shell
curl 'https://smartasset.com/taxes/california-tax-calculator?render=json&' \
  -H 'authority: smartasset.com' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'cookie: _sa_orig_ex=1cCoLzXyg9W6KHjLwbtF6nRKqUWjoSocz73UDMEEjBxtJhIl1qKJ8pIFvcYOjm6Q; _sa_lt=rgd1aKDxAhmKd7R5HTE5TwzkruZMCdJF; _sa_pt=ERmMUwpljmC6SPQBr4lZR9eHbqF2WHxtDW3TlkhuaTnu03mS2C4YVIAP9XCZT4D2; _sa_st_w_mortgagepurchaserates=mrg7FxPg7eR0BNWY4x7UevvI; landingPage=smartasset.com/taxes/massachusetts-tax-calculator; _sa_st=krRNmX5jC5ksPAn1ewojtHff' \
  -H 'origin: https://smartasset.com' \
  -H 'pragma: no-cache' \
  -H 'referer: https://smartasset.com/taxes/california-tax-calculator' \
  -H 'sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest' \
  --data-raw 'ud-it-household-income=140000' \
  --compressed
```
#### Short version that seems to work
```Shell
curl 'https://smartasset.com/taxes/california-tax-calculator?render=json&' \
  -X 'POST' \
  -H 'authority: smartasset.com' \
  --data-raw 'ud-it-household-income=140000' \
  --compressed
```
## Future Features
Can have information on bills passed that year with specific tags to what they relate to. 
- Bill information
- votes for and against
- which tax areas does it touch.
