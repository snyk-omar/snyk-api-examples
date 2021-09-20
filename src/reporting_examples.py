import json
from helpers.client import get_client


def main() -> None:
    client = get_client()

    issue_counts_endpoint = "reporting/counts/issues?from=2021-08-01&to=2021-09-01"
    # data from this endpoint is updated once per hour
    latest_issues_endpoint = (
        "reporting/issues/latest?perPage=100&sortBy=issueTitle&groupBy=issue"
    )
    issue_list_endpoint = "reporting/issues?from=2021-08-01&to=2021-09-01&perPage=100&sortBy=issueTitle&groupBy=issue"
    issue_data = {
        "filters": {
            # required
            "orgs": ["a417db03-e3b7-4bfe-bf08-26f9a802f79b"],
            "severity": [
                "critical",
                "high",
            ],
            "types": ["vuln", "license", "configuration"],
            "languages": [
                "javascript",
                "docker",
                "terraform",
                "python",
            ],
            "projects": [],
            "identifier": "",
            "ignored": False,
            "patched": False,
            "fixable": False,
            "isUpgradable": False,
            "isPatchable": False,
            "isPinnable": False,
            "priorityScore": {"min": 0, "max": 1000},
        }
    }

    # Test issue endpoints
    issue_counts = client.post(issue_counts_endpoint, issue_data).json()
    latest_issues = client.post(latest_issues_endpoint, issue_data).json()
    issue_list = client.post(issue_list_endpoint, issue_data).json()

    print("Issue counts: " + json.dumps(issue_counts, indent=2))
    print("Latest issues: " + json.dumps(latest_issues, indent=2))
    print("Issue list: " + json.dumps(issue_list, indent=2))

    return None


if __name__ == "__main__":
    main()
