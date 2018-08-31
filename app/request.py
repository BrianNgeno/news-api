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

def get_highlights(id)
    get_highlight_details_url = base_url.formart(id,api_key)

    with urllib.request.urlopen(get_highlihts_details_url)as url:
        get_highlights_details = url.read()
        get_highlights_response = json.loads(get_highlights_details)

        highlight_results = None

        if get_highlights_response['results']:
            highlights_results_list = get_highlights_response['results']
            highlights_results = process_results(highlights_results_list)

    return highlights_results


