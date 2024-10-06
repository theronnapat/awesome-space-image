import json
import sys
import requests

class NasaAPI:
    API_ENDPOINT = 'https://api.nasa.gov/planetary/apod?api_key={}'
    FILE_PATH = "./README.md"

    def __init__(self, api_key):
        self._api_key = api_key

    def get_api_key(self):
        return self._api_key

    def fetch_image_data(self):
        try:
            endpoint = self.API_ENDPOINT.format(self._api_key)
            response = requests.get(endpoint, timeout=10)

            response.raise_for_status()

            return response.json()

        except requests.exceptions.Timeout:
            sys.exit("Error: Request timed out.")

        except requests.exceptions.RequestException as e:
            sys.exit(f"Error: Unable to fetch data: {e}")

    def validate_data(self, data):
        required_keys = ['date', 'title', 'url']
        for key in required_keys:
            if key not in data:
                sys.exit(f"Error: {key} not found in data.")

    def write_to_file(self, data, update):
        try:
            with open(self.FILE_PATH, 'w') as file:
                file.write(f"""
# Awesome space image of the day from [NASA](https://api.nasa.gov/)

### Today's image: {data["title"]}
Date: {data["date"]}

![]({data["url"]})

<small>Latest update: {update}</small>
                """)
        except IOError as e:
            sys.exit("Error: Failed to write to file.")
     
    def get_today_image(self, update):
        data = self.fetch_image_data()
        self.validate_data(data)
        self.write_to_file(data, update)