import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

def send_slack_message(text = "データがありません"):

    slack_token = os.getenv("SLACK_API_TOKEN")
    client = WebClient(token=slack_token)
    channel = "#airoco"
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=text
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        print("Error: ", e)
        assert e.response["error"] 