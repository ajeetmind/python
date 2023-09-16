import requests

# GitLab API endpoint to fetch merge request details
# GITLAB_API_URL = "https://gitlab.com/api/v4/projects/<project_id>/merge_requests/<merge_request_iid>"

GITLAB_API_URL = "https://gitlab.com/api/v4/projects/41147841/merge_requests/11"


# GitLab personal access token
GITLAB_TOKEN = "glpat-gg8DkAVvyXzGvQc4ivN1"

# Fetching merge request details from GitLab
response = requests.get(GITLAB_API_URL, headers={"Private-Token": GITLAB_TOKEN})
merge_request = response.json()

print(f"Description: {merge_request['description']}")

