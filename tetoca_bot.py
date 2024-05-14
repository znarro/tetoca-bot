import os
import time
import datetime
from slack import WebClient
from slack.errors import SlackApiError


SLACK_TOKEN = os.environ.get("SLACK_BOT_TOKEN")

TEAM_MEMBERS = [
    "Dario",
    "Diego",
    "Daniel",
    "Jose",
    "Marcelo",
    "Felipe",
    "Zamir",
    "Alvaro",
    "Erick",
    "Mauricio",
    "Maximiliano"
]

CHANNEL_ID = "C05AJ59HG91"


if SLACK_TOKEN is None:
    print("Error: Slack bot token not found. Please set the SLACK_BOT_TOKEN environment variable.")
    exit(1)


# Function to get the next team member in the queue
def get_next_member():
    current_date = datetime.datetime.now()
    week_number = current_date.isocalendar()[1]
    next_member_index = (week_number - 1) % len(TEAM_MEMBERS)
    return TEAM_MEMBERS[next_member_index]


# Function to send a message to Slack
def send_message(message):
    client = WebClient(token=SLACK_TOKEN)
    try:
        response = client.chat_postMessage(
            channel=CHANNEL_ID,
            text=message
        )
        return response["ok"]
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")
        return False
    

# Main function
def main():
    while True:
        # Check if it's Thursday
        if datetime.datetime.now().weekday() == 3:
            # Get the next team member
            next_member = get_next_member()
            message = f"It's {next_member}'s turn this week!"
            
            # Send the message
            if send_message(message):
                print("Message sent successfully!")
            else:
                print("Failed to send message.")
            # Wait for a week
            time.sleep(7 * 24 * 3600)  # Sleep for a week
        else:
            # Check again after a minute if it's not Thursday
            time.sleep(60)


# # Test Main function
# def main():
#     while True:
#         message = "Test every minute"
        
#         # Send the message
#         if send_message(message):
#             print("Message sent successfully!")
#         else:
#             print("Failed to send message.")
        
#         # Wait for a minute
#         time.sleep(60)


if __name__ == "__main__":
    main()