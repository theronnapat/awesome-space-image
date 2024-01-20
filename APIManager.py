import json
import sys
import requests

class NasaAPI:
    def __init__(self, api_key):
        self._api_key = api_key

    def get_api_key(self):
        return self._api_key

    def request(self, endpoint):
        res = requests.get(endpoint)
        if res.status_code == 200:
            data = json.loads(res.text)
            return data
        elif res.status_code == 403:
            raise ValueError("Invalid API Key.\n")
        elif res.status_code == 429:
            raise ValueError("Too many requests, API key exhausted please provide a new API key.\n")

    def get_today_image(self, update):

        endpoint = 'https://api.nasa.gov/planetary/apod?api_key={}'.format(self._api_key)

        data = self.request(endpoint)

        if 'date' not in data:
            sys.exit("Error: date not found in data.\n")

        if 'title' not in data:
            sys.exit("Error: title not found in data.\n")

        if 'url' not in data:
            sys.exit("Error: url not found in data.\n")

        f = open("./README.md", "w")

        f.write(f"""
# Awesome space image of the day from [NASA](https://api.nasa.gov/)

### Today image : {data["title"]}
Date : {data["date"]}

![]({data["url"]})

<small>Latest update : {update}</small>
        """)

        f.close()
