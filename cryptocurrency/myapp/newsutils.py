import  requests
import json

def get_news():
       url = ('https://newsapi.org/v2/everything?'
       'q=bitcoin&'
       'from=2021-03-05&'
       'sortBy=popularity&'
       'apiKey=038c6232441540f385aa4dbf5a7d9bb9')
       response = requests.get(url)

       news=json.loads(response.text)
       print(news)

       return news