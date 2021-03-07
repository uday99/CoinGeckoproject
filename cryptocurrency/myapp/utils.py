import requests

import json



def search_coin():
    resp=requests.get('https://api.coingecko.com/api/v3/coins/list?include_platform=true/')
    coin=json.loads(resp.text)

    #print(coin)

    return coin


def get_detail():
    res = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2Cethereum%2C01coin%2Cstarname%2Ctether%2Cpolkadot%2Cuniswap%2Clitecoin%2Cchainlink%2Clitedog%2Cdogecoin%2Ccosmos%2Cthetfuel&order=market_cap_desc&per_page=100&page=1&sparkline=true')
    detail = json.loads(res.text)

    print(detail)
    return detail

