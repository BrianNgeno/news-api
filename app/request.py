import urllib.request,json
from .models import New

#getting the api_key
api_key = None

#getting the news base_url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    host_url = app.config['ARTICLE_API_BASE_URL']

def get_from_new(category):
    '''
    fuction that gets the jason response to our url request 
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url)as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['sources']:
            new_results_list = get_news_response['sources']
            new_results = process_results(new_results_list)

    return new_results

def get_new(id):
    get_new_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_new_details_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads(new_details_data)

        new_object = None
        if new_details_response.get:
            id = new_details_response.get('id')
            name = new_details_response.get('name')
            url = new_details_response.get('url')
            description = new_details_response.get('description')
            country = new_details_response.get('country')


    return new_object

def process_results(new_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        new_list: A list of dictionaries that contain news details
    Returns :
        new_results: A list of news objects
    '''
    new_results = []
    for new_item in new_list:
        id = new_item.get('id')
        name = new_item.get('name')
        description = new_item.get('description')
        url = new_item.get('url')
        country = new_item.get('country')
      

      
        new_object = New(id,name,description,url,country)
        new_results.append(new_object)

    return new_results

def get_from_articles(articles):
    '''
    fuction that gets the json response to our url request 
    '''
    get_articles_url = host_url.format(name,api_key)

    with urllib.request.urlopen(get_articles_url)as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results(article_results_list)

    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    Args:
        article_list: A list of dictionaries that contain articles details
    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        title = article_item.get('title')
      

      
        article_object = Article(id,name,description,url,urlToImage,publishedAt,title)
        article_results.append(article_object)

    return article_results
