import os
import pprint
import requests
from dotenv import load_dotenv

# Environmental variables
load_dotenv()

api_key = os.getenv("MOVIEDB_API_KEY")
api_key_v4 = os.getenv("MOVIEDB_API_KEY_V4")
# HTTP Requests METHODS

# Endpoints
# GET Movies
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
print(endpoint)
r = requests.get(endpoint)
print(r.status_code)
print(r.text)

#Get Search movie
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
# print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range (200,299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            print(result['title'], _id)
            movie_ids.add(_id)
        # print(list(movie_ids))

#using v4
"""
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
headers= {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'
}
r = requests.get(endpoint, headers=headers)
print(r.status_code)
print(r.text)
"""

# what is the HTTP method that we need?
