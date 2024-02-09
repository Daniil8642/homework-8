from mongoengine import connect
from models import Author, Quote

connect('your_database_name', host='your_mongo_atlas_connection_string')

def search_quotes(query_type, query_value):
    if query_type == 'name':
        author = Author.objects(fullname__icontains=query_value).first()
        if author:
            quotes = Quote.objects(author=author)
            return [quote.quote for quote in quotes]
    elif query_type == 'tag':
        quotes = Quote.objects(tags__icontains=query_value)
        return [quote.quote for quote in quotes]
    elif query_type == 'tags':
        tags = query_value.split(',')
        quotes = Quote.objects(tags__in=tags)
        return [quote.quote for quote in quotes]
    else:
        return []

if __name__ == '__main__':
    while True:
        user_input = input("Enter command: ").split(':')
        query_type, query_value = user_input[0], user_input[1]
        if query_type == 'exit':
            break
        results = search_quotes(query_type, query_value)
        print(results)

import json
from mongoengine import connect
from models import Author, Quote
import redis

connect('your_database_name', host='your_mongo_atlas_connection_string')
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def search_quotes(query_type, query_value):
    cache_key = f"{query_type}:{query_value}"
    cached_result = redis_client.get(cache_key)
    if cached_result:
        return json.loads(cached_result)
    
    if query_type == 'name':
        author = Author.objects(fullname__icontains=query_value).first()
        if author:
            quotes = Quote.objects(author=author)
            result = [quote.quote for quote in quotes]
    elif query_type == 'tag':
        quotes = Quote.objects(tags__icontains=query_value)
        result = [quote.quote for quote in quotes]
    elif query_type == 'tags':
        tags = query_value.split(',')
        quotes = Quote.objects(tags__in=tags)
        result = [quote.quote for quote in quotes]
    else:
        result = []
    
    redis_client.set(cache_key, json.dumps(result))
    return result

if __name__ == '__main__':
    while True:
        user_input = input("Enter command: ").split(':')
        query_type, query_value = user_input[0], user_input[1]
        if query_type == 'exit':
            break
        results = search_quotes(query_type, query_value)
        print(results)
