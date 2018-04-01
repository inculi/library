from urllib.parse import quote_plus
import json
from pprint import pprint

import requests

from config import API_KEY

def gbooks_search(queryString):
    global API_KEY
    
    queryPayload = {
        'q' : quote_plus(queryString),
        'key' : API_KEY
    }

    url = 'https://www.googleapis.com/books/v1/volumes'
    r = requests.get(url, params=queryPayload)
    data = json.loads(r.content)

    def simplify_book_json(b):
        book = b.get('volumeInfo', {})

        bookDict = {
            # str
            'title' : book.get('title', 'Title Unknown'),
            'subtitle' : book.get('subtitle', ''),
            'publisher' : book.get('publisher', 'Publisher Unknown.'),
            'publishedDate' : book.get('publishedDate'),
            'descr' : book.get('description', ''),
            'abstract' : b.get('searchInfo', {}).get('textSnippet', ''),
            'thumbnail' : book.get('imageLinks', {}).get('smallThumbnail'),

            # list
            'authors' : book.get('authors', []),
            'categories' : book.get('categories', []),

            # float
            'rating' : book.get('averageRating', None)
        }

        if not bookDict['thumbnail']:
            bookDict['thumbnail'] = book.get('imageLinks', {}).get('thumbnail')
        
        return bookDict
    
    return [simplify_book_json(b) for b in data['items']]

if __name__ == "__main__":
    # Just to test stuffs :)
    data = gbooks_search('machine learning')
    pprint(data)
