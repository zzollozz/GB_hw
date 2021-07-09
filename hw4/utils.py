import requests
from decimal import Decimal

def currency_rates(val):
    r = requests.get('http://www.cbr-xml-daily.ru/daily_json.js')
    data = r.headers['Date']
    r = r.json()

    if not r['Valute'].get(val.upper()):
        print('None')
        return
    n = Decimal(r["Valute"][val.upper()]["Value"]).quantize(Decimal("1.00"))

    print(f'{val.upper()}  "{r["Valute"][val.upper()]["Name"]}": {n}     Date: {data}')

if __name__ == '__main__':
    currency_rates('AMD')
    currency_rates('usd')
    currency_rates('EuR')
