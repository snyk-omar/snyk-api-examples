import json
from helpers.client import get_client, get_config


def main() -> None:
    config = get_config()
    project_id = config["PROJECT_ID"]
    org_id = config["ORG_ID"]
    client = get_client()
    # This is actually deprecated it seems. Do not use
    # project = client.projects.get(project_id)
    # vulns = project.vulnerabilities.all()

    data = {
        "includeDescription": False,
        "includeIntroducedThrough": True,
        "filters": {
            "severities": [
                "critical",
                "high",
                # "medium",
                # "low"
            ],
            "exploitMaturity": [
                "mature",
                "proof-of-concept",
                # "no-known-exploit",
                # "no-data"
            ],
            "types": [
                "vuln",
                # "license"
            ],
            "ignored": False,
            "patched": False,
            "priority": {"score": {"min": 700, "max": 1000}},
        },
    }

    resp = client.post(f"org/{org_id}/project/{project_id}/aggregated-issues", data)
    issues = resp.json()["issues"]
    for issue in issues:
        print(json.dumps(issue, indent=2))

    return None


if __name__ == "__main__":
    main()
