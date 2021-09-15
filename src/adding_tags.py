from helpers.client import get_client


def main() -> None:
    # ord id for the red js node org
    project_id = "c2fc48a2-159a-4f1f-886f-54f4b77a0be6"
    client = get_client()

    project = client.projects.get(project_id)

    # print(project.tags.add('cool', 'project'))
    # print(project.tags.delete('cool', 'project'))
    print(project.tags.all())


if __name__ == "__main__":
    main()
