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
    # Here is how you can fetch your orgs by the name of the group
    # You can also use the group ID
    config = create_config()
    client = create_client(config["API_TOKEN"])
    organizations = client.organizations.all()
    orgs = []
    for org in organizations:
        if org.group is not None:
            if org.group.name == "Pandánte, Inc.":
                orgs.append(org)

    print(orgs)


if __name__ == "__main__":
    main()
