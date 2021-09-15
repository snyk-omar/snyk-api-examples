from helpers.client import get_client


def main() -> None:
    client = get_client()
    print(client)
    return None


if __name__ == "__main__":
    main()
