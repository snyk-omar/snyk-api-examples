from helpers.client import get_client, get_config


def main() -> None:
    client = get_client()
    config = get_config()
    group_id = config["GROUP_ID"]
    query_string = "from=2021-08-01&to=2021-09-20"
    audit_logs_endpoint = f"group/{group_id}/audit?{query_string}"

    filter_values = {
        "filters": {
            "userId": "",
            "email": "",
            "event": "org.project.add",
            "excludeEvent": "",
            "projectId": "",
        }
    }

    results = client.post(audit_logs_endpoint, filter_values).json()
    for result in results:
        print(result["content"], result["created"], result["orgId"])

    return None


if __name__ == "__main__":
    main()
