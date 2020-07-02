# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

# change cookie to yours
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': 'ALF=1596268309; SCF=AgUvjZtFMfewo8LphsFHOZx1XqZfgL3mwkzMzlA0xpQNqwkUGUgLwHnUzgnrnsPC7YWJWG7h4CSufYZPBRTfbA4.; SUB=_2A25z-ejXDeRhGeBG6VsZ9CzKwjWIHXVRBYifrDV6PUJbktAKLWfDkW1NRg52giDqHSlCxrnSS8fDELdQsEV3s4cW; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whj2YXN4Z_2g4SWgzAbf-ZG5JpX5K-hUgL.FoqReo.RShzc1K.2dJLoIEBLxK-L1K2L1hqLxK-L1K2L1hqLxK-LBonLBKqLxK-LBKBLBKMt; SUHB=0sqBkkXbWJlqWz; SSOLoginState=1593677959; _T_WM=16f36a29a948feaf9cd547fd90b8cb56',
}

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    #'pipelines.MongoDBPipeline': 300,
     'pipelines.JsonPipeline': 300,
}

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017