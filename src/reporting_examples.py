import concurrent.futures
import json
from helpers.client import get_client


client = get_client()

issue_counts_endpoint = "reporting/counts/issues?from=2021-08-01&to=2021-09-01"
# data from this endpoint is updated once per hour
latest_issues_endpoint = (
    "reporting/issues/latest?perPage=100&sortBy=issueTitle&groupBy=issue"
)
issue_list_endpoint = "reporting/issues?from=2021-08-01&to=2021-09-01&perPage=100&sortBy=issueTitle&groupBy=issue"
issue_filter = {
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

endpoints = [issue_counts_endpoint, issue_list_endpoint, latest_issues_endpoint]
issue_filters = [issue_filter for _ in range(3)]


def get_report_data(endpoint: str, issue_filter: dict) -> dict:
    json_resp = client.post(endpoint, issue_filter).json()
    print(json.dumps(json_resp, indent=2))


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        print("Staring...")
        executor.map(get_report_data, endpoints, issue_filters)
