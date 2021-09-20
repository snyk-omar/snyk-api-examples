from helpers.client import get_client, get_config


def main() -> None:
    client = get_client()
    config = get_config()
    # Using the group ID GUID
    group_id = config["GROUP_ID"]

    # iterating through the list of orgs and adding my orgs to a list
    organizations = client.organizations.all()
    my_orgs = []
    for org in organizations:
        if org.group is not None:
            if org.group.id == group_id:
                my_orgs.append(org)

    print(my_orgs)


if __name__ == "__main__":
    main()
