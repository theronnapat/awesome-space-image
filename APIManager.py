import requests
import sys

class NasaAPI:
    def __init__(self, api_key):
        self._api_key = api_key

    def get_today_image(self, update):
        try:
            # API endpoint
            endpoint = f'https://api.nasa.gov/planetary/apod?api_key={self._api_key}'

            # Making the request
            res = requests.get(endpoint)

            # Check for request errors
            if res.status_code != 200:
                sys.exit(f"Error: Failed to fetch data, status code {res.status_code}.\n")

            # Parse response JSON
            data = res.json()

            # Validating necessary keys in response data
            if 'date' not in data or 'title' not in data or 'url' not in data:
                sys.exit("Error: Required fields (date, title, url) not found in data.\n")

            # Writing to README.md
            with open("./README.md", "w") as f:
                f.write(f"""
# Awesome space image of the day from [NASA](https://api.nasa.gov/)

### Today image : {data["title"]}
Date : {data["date"]}

![]({data["url"]})

<small>Latest update : {update}</small>
                """)

        except Exception as e:
            sys.exit(f"An error occurred: {e}")
