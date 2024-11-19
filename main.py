import os
import sys
import datetime
from dotenv import load_dotenv
from APIManager import NasaAPI

# Minimum required Python version
MIN_PYTHON = (3, 0)

def check_python_version():
    """Check if the current Python version meets the minimum requirement."""
    if sys.version_info < MIN_PYTHON:
        raise RuntimeError(f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or later is required.")

def load_api_key():
    """Load API key from the environment variables."""
    load_dotenv()
    api_key = os.getenv("API")
    
    if not api_key:
        raise ValueError("API key is missing. Please ensure it's present in the .env file.")
    
    return api_key

def get_current_timestamp():
    """Return the current timestamp formatted as a string."""
    return datetime.datetime.now().strftime("%c")

def main():
    """Main function to fetch the NASA image for today."""
    try:
        # Check Python version
        check_python_version()
        
        # Load API key
        api_key = load_api_key()
        
        # Get the current timestamp
        update_time = get_current_timestamp()
        
        # Initialize the NASA API client
        nasa_api = NasaAPI(api_key=api_key)
        
        # Fetch today's image from the NASA API
        response = nasa_api.get_today_image(update=update_time)
        
        # Log or display the response (assuming response handling is done inside get_today_image)
        print("NASA Image for today:", response)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
