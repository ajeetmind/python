import os
import subprocess
import slack
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

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
        output = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT)
    except FileNotFoundError:
        output = f"File not found: {code_file_path}"
    except subprocess.CalledProcessError as e:
        output = e.output
    except Exception as e:
        output = str(e)
    finally:
        respond(output)

if __name__ == "__main__":
    handler = SocketModeHandler(app_token=SLACK_APP_TOKEN, app=app)
    handler.start()
