import requests


import json

def get_list():
    response=requests.get('https://api.coingecko.com/api/v3/coins/list')
    d1=json.loads(response.text)

    my=d1
    print(my)
    val=[x['id'] for x in my if 'id' in x]
    print(val)

    for i in val:
        print(i ,end=',')



    return  d1


# mylist = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
# myvalues = [i['d'] for i in mylist if 'd' in i]


# response=requests.get('https://api.coingecko.com/api/v3/coins/list')
# d1=json.loads(response.text)
# my=d1
# print(my)
# val=[x['id'] for x in my if 'id' in x]
# print(val)
#
# for i in val:
#     print(i ,end=',')
#
#
