import os
'''
this helps get the api base url and key from the remote
'''
def Config():
    '''
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?api_key={}'
    NEWS_API_KEY = os.environment.get('NEWS_API_KEY')
    SECRET_KEY = os.environment.get('SECRET_KEY')
    @staticmethod
    def init_app(app):
        pass

def ProdConfig(Config):
    pass

def DevConfig(Config):
    DEBUG True
    config_option ={
        'production'= ProdConfig,
        'development' = DevConfig
    }