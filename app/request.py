import urllib.request,json
from .models import News

#getting the api_key
api_key = None

#getting the news base_url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_new(category):
    '''
    fuction that gets the jason response to our url request 
    '''
    get_news_url = base_url.formart(category,api_key)

    with urllib.request.urlopen(get_news_url)as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['results']:
            new_results_list = get_news_response['results']
            new_results = process_results(new_results_list)

    return new_results

def get_new(id):
    get_new_details_url = base_url.formart(id,api_key)

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