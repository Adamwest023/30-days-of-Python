import requests

ngrok_url = "https://a7d8-2601-481-8401-ee90-685d-b18e-32c7-9383.ngrok.io"
endpoint = f"{ngrok_url}/box-office-mojo-scraper"

r = requests.post(endpoint, json={})
print(r.json()['data'])