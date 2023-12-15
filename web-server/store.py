import requests
URL = 'https://api.escuelajs.co/api/v1/'

def get_categories():
    r = requests.get(f'{URL}categories')
    categories = r.json()
    for category in categories:
        print(category['name'])