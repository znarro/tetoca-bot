import os
import time
import datetime
from slack import WebClient
from slack.errors import SlackApiError

SLACK_TOKEN = "your-slack-bot-token"

TEAM_MEMBERS = ["Zamir", "Alvaro", "Dario"]

CHANNEL_ID = ""