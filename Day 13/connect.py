import os
import requests
from dotenv import load_dotenv

#Environmental variables
load_dotenv()

api_key =os.getenv("MOVIEDB_API_KEY")

# HTTP Requests METHODS 
  
# Endpoint 
"""
GET
/movie/{movie_id}
https://api.themoviedb.org/3/movie/{movie_id}?api_key=api_key
"""
movie_id = 500 
api_version = 3 
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
print(endpoint)
r = requests.get(endpoint)
print(r.status_code)
print(r.text)

# what is the HTTP method that we need?