import os
'''
this helps get the api base url and key from the remote
'''
class Config():
    '''
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

@staticmethod
def init_app(app):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options ={
    'development':DevConfig,
    'production':ProdConfig
    
}
