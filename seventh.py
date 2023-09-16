import os
import slack
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def handle_mention(event, say):
    prompt = event["text"].replace(event["bot_profile"]["name"], "").strip()
    if prompt:
        try:
            response = openai.Completion.create(engine="davinci-codex", prompt=prompt, max_tokens=1024, n=1)
            output = response.choices[0].text
            say(output)
        except Exception as e:
            say(str(e))

if __name__ == "__main__":
    handler = SocketModeHandler(app_token=SLACK_APP_TOKEN, app=app)
    handler.start()
