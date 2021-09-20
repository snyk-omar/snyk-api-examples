import snyk
from dotenv import dotenv_values


def get_config():
    return dotenv_values()


def get_client():
    config = get_config()
    token = config["API_TOKEN"]
    return snyk.SnykClient(token)
