import os
from dotenv import load_dotenv

from flask import Flask, render_template
import requests

from utils.get_apod import get_apod

# Load the environment variables from .env file
load_dotenv()
nasa_api_key = os.environ["NASA_API_KEY"]

# Create the Flask application
app = Flask(__name__)


@app.route('/')
def home():
    api_key = nasa_api_key
    apod_data, error = get_apod(api_key)
    if error:
        return f"Error: {error}"
    return render_template('index.html', apod=apod_data)
    # return render_template('templates/index.html', apod=apod_data)


if __name__ == '__main__':
    app.run(debug=True)
