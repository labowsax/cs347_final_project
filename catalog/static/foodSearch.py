# services/weather_service.py
import requests
import logging

logger = logging.getLogger(__name__)


def get_food_data(query):
    try:
        url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key=ZYIHMGpSmgzwCecsbSxa7rSNizrdeitAiug86jlZ&query={query}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to retrieve food data: {e}")
        return None
