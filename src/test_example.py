from helpers.client import get_client


def main() -> None:
    client = get_client()
    # Using the group ID GUID
    group_id = "aaa10401-c024-4046-8bfa-3900bf988db8"

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
