# -------------------- Step 1: Import Required Libraries --------------------
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# -------------------- Step 2: Twilio Account Setup --------------------
# Obtain your Account SID and Auth Token from the Twilio Dashboard
account_sid = "(somealphanumeric code given by twilio)"   # Replace with your Twilio Account SID
auth_token = "(some alphanumeric values given by twilio)"       # Replace with your Twilio Auth Token

# Initialize Twilio Client
client = Client(account_sid, auth_token)

# -------------------- Step 3: Define Function to Send WhatsApp Message --------------------
def send_whatsapp_message(recipient_number, message_body):
    """
    Sends a WhatsApp message to the given recipient number using Twilio API.
    """
    try:
        message = client.messages.create(
            from_='whatsapp:(number given by twilio)',  # Twilio Sandbox Number
            body=message_body,
            to=f"whatsapp:{recipient_number}"
        )
        print(f"✅ Message sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print(f"⚠ An error occurred while sending message: {e}")

# -------------------- Step 4: Take User Inputs --------------------
print("===== Automated WhatsApp Text Generator =====\n")

# Get recipient details and message
name = input("Enter the Recipient Name: ")
recipient_number = input("Enter the Recipient WhatsApp Number with country code (e.g., +919876543210): ")
message_body = input(f"Enter the message you want to send to {name}: ")

# -------------------- Step 5: Get Date and Time for Scheduling --------------------
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')

# Combine and convert date & time into datetime object
scheduled_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# -------------------- Step 6: Calculate Time Difference --------------------
time_difference = scheduled_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

# -------------------- Step 7: Validate and Schedule Message --------------------
if delay_seconds <= 0:
    print("⚠ The specified time is in the past. Please enter a valid future date and time.")
else:
    print(f"\n📅 Message scheduled to be sent to {name} at {scheduled_datetime}.")
    print("⏳ Waiting for the scheduled time...\n")

    # Wait until the scheduled time
    time.sleep(delay_seconds)

    # -------------------- Step 8: Send Message Automatically --------------------
    send_whatsapp_message(recipient_number, message_body)

    # -------------------- Step 9: Confirmation --------------------
    print(f"✅ WhatsApp message sent successfully to {name} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")

# -------------------- Step 10: End of Program --------------------
print("\n===== Program Completed Successfully =====")
