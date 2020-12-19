import urllib.request,json
from app.models import Quote


def my_quotes():
    get_quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_quote_url) as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)

        quote_object = None
        
        if quote_details_response:
            id = quote_details_response.get('id')
            author = quote_details_response.get('author')
            quote = quote_details_response.get('quote')
            permalink = quote_details_response.get('permalink')
            
            quote_object = Quote(id, author, quote, permalink)
    return quote_object

