from helpers.client import get_client, get_config


def main() -> None:
    # ord id for the red js node org
    config = get_config()
    project_id = config["PROJECT_ID"]
    client = get_client()

    project = client.projects.get(project_id)

    # print(project.tags.add('cool', 'project'))
    # print(project.tags.delete('cool', 'project'))
    print(project.tags.all())


if __name__ == "__main__":
    main()
