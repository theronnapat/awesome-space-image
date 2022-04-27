import requests, json, random
from dotenv import load_dotenv
import os

load_dotenv()

apikey = os.getenv("API")

f = open("./README.md", "w")

link = 'https://api.nasa.gov/planetary/apod?api_key={}'.format(apikey)

res = requests.get(link)
data = json.loads(res.text)


f.write(f'''
# Awesome space image of the day from [nasa](https://api.nasa.gov/)

### Today image : {data['title']}

Date : {data['date']}

![]({data['url']})


''')

f.close()