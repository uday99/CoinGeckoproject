# from newsapi import NewsApiClient
#
# # Init
# newsapi = NewsApiClient(api_key='038c6232441540f385aa4dbf5a7d9bb9')
#
# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')
#
# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)
#
# # /v2/sources
# sources = newsapi.get_sources()
# # print(top_headlines)
# # print(all_articles)