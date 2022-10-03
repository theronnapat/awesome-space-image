import os
import sys
import datetime
from dotenv import load_dotenv
from APIManager import NasaAPI


MIN_PYTHON = (3, 0)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

load_dotenv()

API_KEY = os.getenv("API")


if __name__ == '__main__':
    x = datetime.datetime.now()
    update = x.strftime("%c")

    nasaAPI = NasaAPI(api_key=API_KEY)
    nasaAPI.get_today_image(update=update)

