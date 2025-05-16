import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

def send_slack_message(text = "データがありません",channel_int = 0):

    slack_token = os.getenv("SLACK_API_TOKEN")
    client = WebClient(token=slack_token)
    channel = ""
    if channel_int == 301:
        channel = "#r3-301"
    elif channel_int == 401:
        channel = "#r3-401"
    elif channel_int == 403:
        channel = "#r3-403"
    else:
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