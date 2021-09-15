import snyk
from dotenv import dotenv_values


def get_api_token():
    config = dotenv_values()
    return config["API_TOKEN"]


def get_client():
    token = get_api_token()
    return snyk.SnykClient(token)
