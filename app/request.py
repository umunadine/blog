import urllib.request,json
from .models import Quotes

base_url=None

def configure_request(app):
    global base_url
    base_url = app.config["QUOTES_API_BASE_URL"]

def my_quotes():
    get_quotes_url = base_url

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None
        quotes_results_list = get_quotes_response
        quotes_results = process_results(quotes_results_list)


    return quotes_results

def process_results(quotes_list):
    
    quotes_results = []
    for quotes_item in quotes_list:
        author = quotes_item.get('author')
        quote = quotes_item.get('quote')
        permalink = quotes_item.get('permalink')

        if author:
            quotes_object = Quotes(author,quote,permalink)
            quotes_results.append(quotes_object)

    return quotes_results


