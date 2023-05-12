from dotenv import load_dotenv
import os
import requests
from PIL import Image
from io import BytesIO

# Load .env file
load_dotenv()

API_KEY = os.getenv('NASA_API_KEY')

def fetch_apod():
    base_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': API_KEY
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        image_url = data['url']
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        image.show()
    else:
        print(f"Error getting APOD, status code: {response.status_code}")

if __name__ == '__main__':
    fetch_apod()