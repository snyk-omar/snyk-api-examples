from helpers.client import get_client, get_config


def main() -> None:
    client = get_client()
    config = get_config()

    org_id = config["ORG_ID"]

    # List webhooks endpoint
    endpoint = f"org/{org_id}/webhooks"
    resp = client.get(endpoint)
    print(resp.json())

    return None


if __name__ == "__main__":
    main()
