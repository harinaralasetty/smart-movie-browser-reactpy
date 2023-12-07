import requests
import json

# Load API key from config.json
with open('config.json') as config_file:
    config_data = json.load(config_file)

api_key = config_data['movie_api']['apikey']

import aiohttp

async def fetch_movies():
    try:
        url = f'https://api.themoviedb.org/3/discover/movie'
        params = {'api_key': api_key}
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                data = await response.json()
                print('got it ========================================>>>>>>')
                return data.get('results', [])
    except Exception as error:
        print('Error fetching movies:', error)
        return []

def search_movies(query):
    try:
        url = f'https://api.themoviedb.org/3/search/movie'
        params = {'api_key': api_key, 'query': query}
        response = requests.get(url, params=params)
        data = response.json()
        return data['results']
    except Exception as error:
        print('Error fetching movies:', error)
        return []

# top_movies = fetch_movies()
# print("Top Movies:", top_movies)

# search_term = 'Spider-Man'
# search_results = search_movies(search_term)
# print(f"Search Results for '{search_term}':", search_results)
