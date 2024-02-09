import json
from mongoengine import connect
from models import Author, Quote

connect('your_database_name', host='your_mongo_atlas_connection_string')

def load_authors():
    with open('authors.json', 'r', encoding='utf-8') as file:
        authors_data = json.load(file)
        for author_data in authors_data:
            Author(**author_data).save()

def load_quotes():
    with open('quotes.json', 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)
        for quote_data in quotes_data:
            author_name = quote_data['author']
            author = Author.objects(fullname=author_name).first()
            if author:
                quote_data['author'] = author
                Quote(**quote_data).save()

if __name__ == '__main__':
    load_authors()
    load_quotes()
