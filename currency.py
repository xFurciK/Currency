import requests
import json
from matplotlib import pyplot as plt

option_choose = int(input('''
Choose operation you want to do, type:
1 to check rates
2 to convert one currency to another
3 to see a exchange rate chart
'''))

def rate_check():
    try:
        currency = input('Enter currency you want to check (GBP, PLN, EUR etc.): ')
        url = f'https://api.nbp.pl/api/exchangerates/rates/c/{currency}/today/?format=json'
        response = requests.get(url)
        json_data = json.loads(response.text)
        return round(json_data['rates'][0]['bid'], 2)
    except:
        return 'Invalid currency shortcut'
def converter():
    try:
        source_currency = input('Enter currency you want to convert (EUR, GBP etc,): ')
        source_currency_amount = int(input('Enter amount of currency you want to convert: '))
        target_currency = input('Enter currency in which you want the result (GBP, EUR etc.): ')

        source_response = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/{source_currency}/today/?format=json')
        source_json_data = json.loads(source_response.text)

        target_response = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/{target_currency}/today/?format=json')
        target_json_data = json.loads(target_response.text)

        scaler = source_json_data['rates'][0]['ask']/target_json_data['rates'][0]['ask']
        return round(source_currency_amount * scaler, 2)
    except:
        return 'Number was not typed or invalid shortcut'

def exchange_rate_chart():
    try:
        currency = input('Enter currency you want to check (GBP, PLN, EUR etc.): ')
        period_length = int(input('Enter period length: '))
        response = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/last/{period_length}/?format=json')
        data = json.loads(response.text)
        rates = [data['rates'][rate]['mid'] for rate in range(len(data['rates']))]
        dates = [data['rates'][date]['effectiveDate'] for date in range(len(data['rates']))]
        plt.plot(dates, rates)
        plt.ylabel('Exchange rate')
        plt.xlabel('Date')
        plt.show()
    except:
        return 'Number was not typed or invalid shortcut'

if option_choose == 1:
    print('Kurs wynosi: ', rate_check())
elif option_choose == 2:
    print('Przeliczona kwota wynosi: ',converter())
elif option_choose == 3:
    print(exchange_rate_chart())
