import requests


def get_apod(api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    try:
        response = requests.get(url, params={'api_key': api_key})
        response.raise_for_status()
        data = response.json()
        return {
            "media_type": data.get("media_type"),
            "url": data.get("url"),
            "title": data.get("title"),
            "date": data.get("date"),
            "description": data.get("explanation"),
        }, None
    except Exception as e:
        return None, e
