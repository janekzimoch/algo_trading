from coinapi_rest_v1.restapi import CoinAPIv1
import requests
import json

# python examples.py 5984A9EA-8AA7-4444-ABDB-3714E8BD29C3




# # Get the historical exchange rates between two assets in the form of the timeseries.
# limit = 1000
# url = f'https://rest.coinapi.io/v1/exchangerate/BTC/USD/history?period_id=10DAY&time_start=2016-01-01T00:00:00&time_end=2020-02-01T00:00:00&limit={limit}'
# headers = {'X-CoinAPI-Key' : '5984A9EA-8AA7-4444-ABDB-3714E8BD29C3',
#            'Accept': 'application/json'}
# response = requests.get(url, headers=headers)

# with open('./BTC_USD_timeseries.json', 'w', encoding='utf-8') as f:
#     json.dump(response.json(), f, ensure_ascii=False, indent=4)


# get current order book for bitcoin
limit = 1000
url = f'https://rest.coinapi.io/v1/orderbooks/BITSTAMP_SPOT_BTC_USD/latest/limit={limit}'
headers = {'X-CoinAPI-Key' : '5984A9EA-8AA7-4444-ABDB-3714E8BD29C3',
           'Accept': 'application/json'}
response = requests.get(url, headers=headers)

with open('./BTC_USD_orderbook_latest.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)