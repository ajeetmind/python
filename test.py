import os
import logging
import requests
import json



SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]
SLACK_CHANNEL = os.environ["SLACK_CHANNEL"]
MERGE_REQUEST_IID = os.environ["MERGE_REQUEST_IID"]
PROJECT_URL = os.environ.get("CI_PROJECT_URL")
PROJECT_BRANCH = os.environ.get("CI_COMMIT_BRANCH")

# Set up logging
logging.basicConfig(level=logging.INFO)

# create Merge URL
MERGE_URL = f"{PROJECT_URL}/-/merge_requests/{MERGE_REQUEST_IID}"

# Build the Slack message payload
if os.environ.get("CI_COMMIT_BRANCH") == "production":
    payload = {
        "text": f"{PROJECT_BRANCH} : {MERGE_URL} is merged!\n kindly restart application",
        "channel": "#devops"
    }
else:
    payload = {
        "text": f"{PROJECT_BRANCH} : Merge {MERGE_URL} is merged!",
        "channel": SLACK_CHANNEL
    }


# Send the Slack message
response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload))

if response.status_code != 200:
    logging.error(f"Failed to send Slack message: {response.text}")
else:
    logging.info("Slack message sent successfully.")
