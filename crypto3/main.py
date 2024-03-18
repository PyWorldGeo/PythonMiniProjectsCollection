import api_key
import requests
import time

def get_info(my_coins):
    """Returns Realtime Info For Desired Coins"""
    headers = {
        "X-CMC_PRO_API_KEY": api_key.key,
        "Accepts": "application/json"
               }
    params = {
        'start': '1',
        'limit': '1000',
        'convert': 'USD'
    }
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    json_data = requests.get(url, params=params, headers=headers).json()
    coins = json_data['data']
    data = []
    for x in coins:
        if x['symbol'] in my_coins:
            # data[x['symbol']] = x['quote']['USD']['price']
            obj = {"name": x['symbol'], "price": x['quote']['USD']['price']}
            data.append(obj)

    return data


def show_crypto():
    my_coins = ["BTC", "ETH", "BNB", "SOL"]

    refresh_time = 60
    pause = False
    start = time.time()

    run = True
    while run:
        if not pause:
            new_data = get_info(my_coins)
            pause = True
            end = start + refresh_time

            for obj in new_data:
                print(f"{obj['name']}: {obj['price']} USD")
            print()

        if time.time() >= end:
            start = time.time()
            pause = False

if __name__ == "__main__":
    show_crypto()














