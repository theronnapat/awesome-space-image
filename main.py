# Import necessary libraries
import os
import sys
import datetime
from dotenv import load_dotenv
from APIManager import NasaAPI  # Assuming there's a custom module named 'APIManager' for NASA API interaction

# Define the minimum required Python version as (3, 0)
MIN_PYTHON = (3, 0)

# Check if the current Python version is less than the required version
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

# Load environment variables from a .env file (if present)
load_dotenv()

# Retrieve the API key from the environment variables
API_KEY = os.getenv("API")

# Check if the API key is missing, and exit the program if it is
if API_KEY is None:
    sys.exit("API key is required.\n")

# Entry point of the script
if __name__ == '__main__':
    # Get the current date and time
    x = datetime.datetime.now()
    
    # Format the current date and time as a string in a specific format ("%c")
    update = x.strftime("%c")

    # Create an instance of the NasaAPI class with the provided API key
    nasaAPI = NasaAPI(api_key=API_KEY)

    # Call the 'get_today_image' method of the NasaAPI instance and pass the 'update' parameter
    # This function likely interacts with NASA's API to retrieve today's image or information
    nasaAPI.get_today_image(update=update)
