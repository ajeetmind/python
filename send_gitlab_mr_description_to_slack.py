import os
import requests
import json

# GITLAB_API_TOKEN = os.environ["GITLAB_API_TOKEN"]
# SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]
# SLACK_CHANNEL = os.environ["SLACK_CHANNEL"]
# PROJECT_ID = os.environ["PROJECT_ID"]

GITLAB_API_TOKEN = ""
SLACK_WEBHOOK_URL = ""
SLACK_CHANNEL = "#test"
PROJECT_ID = "41147841"
MERGE_REQUEST_ID = 71
# Set the GitLab API endpoint and merge request ID
GITLAB_API_ENDPOINT = "https://gitlab.com/api/v4"
# MERGE_REQUEST_ID = os.environ["CI_MERGE_REQUEST_IID"]

# Get the merge request details from GitLab
url = f"{GITLAB_API_ENDPOINT}/projects/{PROJECT_ID}/merge_requests/{MERGE_REQUEST_ID}"
print(f"{url}")
headers = {"Private-Token": GITLAB_API_TOKEN}
response = requests.get(url, headers=headers)
merge_request = response.json()
# print(f"{merge_request}")

# Get the merge request description
description = merge_request["description"]

# Build the Slack message payload
payload = {
    "text": f"Merge Request Description: {description}",
    "channel": SLACK_CHANNEL,
}

# Send the Slack message
# response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload))

if response.status_code != 200:
    print(f"Failed to send Slack message: {response.text}")
else:
    print("Slack message sent successfully.")



"""
stages:
  - notify

notify:
  stage: notify
  image: python:3.10-slim-buster
  variables:
    SLACK_WEBHOOK_URL: "https://hooks.slack.com/services/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"
    SLACK_CHANNEL: "#k8s-alerts"  # replace with your Slack channel name
  script:
    - pip install requests
    - python send_gitlab_mr_description_to_slack.py
  only:
     variables:
      - $CI_COMMIT_MESSAGE =~ /Merge.+branch\s(.*)\sinto(.*)/  && ('$CI_COMMIT_BRANCH == "main"'  && '$CI_COMMIT_BRANCH == "test"') 


"""