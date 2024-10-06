import os
import sys
import datetime
from dotenv import load_dotenv
from APIManager import NasaAPI

load_dotenv()
MIN_PYTHON = (3, 0)

def check_python_version():
    if sys.version_info < MIN_PYTHON:
        sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

def load_api_key():
    api_key = os.getenv("API")
    if api_key is None:
        sys.exit("API key is required.\n")
    return api_key

if __name__ == '__main__':
    check_python_version()

    api_key=load_api_key()

    current_time = datetime.datetime.now()
    update = current_time.strftime("%c")
    
    try:
        nasaAPI = NasaAPI(api_key=api_key)
        nasaAPI.get_today_image(update=update)
    except Exception as e:
        sys.exit("Error trying to fetch and write NASA image of the day. \n")