import os
import random
from flask import Flask
from slack import webclient
from slackeventsapi import SlackEventAdapter


app = Flask(__name__)

slack_web_client = webclient(token=os.environ.get("SLACK_BOT_TOKEN"))

MESSAGE_BLOCK = {

  }

@app.route("/")

def helloworld():
    return("Hello world")

if __name__ ==  "__main__":
    app.run(host="0.0.0.0", port=8081)