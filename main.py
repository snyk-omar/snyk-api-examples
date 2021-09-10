import snyk
from dotenv import dotenv_values


def create_config() -> dict:
    return dotenv_values(".env")


def create_client(api_token: str = None) -> snyk.SnykClient:
    if api_token is None:
        raise ValueError
    client = snyk.SnykClient(api_token)
    return client


def main() -> None:
    config = create_config()
    client = create_client(config["API_TOKEN"])
    print(client.organizations.first().projects.all())


if __name__ == "__main__":
    main()
