import os
import subprocess
import slack
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN)

@app.command("/execute-python")
def handle_execute_python_command(ack, body, respond):
    code_file_path = body["text"].strip()
    output = ""
    try:
        with open(code_file_path, "r") as f:
            code = f.read()
        response = openai.Completion.create(engine="davinci-codex", prompt=code, max_tokens=1024, n=1)
        output = response.choices[0].text
    except FileNotFoundError:
        output = f"File not found: {code_file_path}"
    except Exception as e:
        output = str(e)
    finally:
        respond(output)

if __name__ == "__main__":
    handler = SocketModeHandler(app_token=SLACK_APP_TOKEN, app=app)
    handler.start()
