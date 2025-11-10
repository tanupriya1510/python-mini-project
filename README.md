📌 Overview
This project demonstrates how automation and API integration can simplify real-world communication tasks.
Using Python and the Twilio API, it allows users to automatically send WhatsApp messages without manual effort.
The system can send instant or scheduled messages with ease — making it ideal for reminders, alerts, or simple automation tasks.

⚙ Requirements
Before running this project, make sure you have:
Python 3.8 or above installed
A Twilio account with WhatsApp sandbox access
The following Python library installed:
pip install twilio

🚀 How to Run
Get your Twilio credentials:
Log in to your Twilio Console.
Copy your Account SID and Auth Token.
Go to the Messaging → Try it out → WhatsApp Sandbox section and copy your Twilio WhatsApp Number.

Update the Python file:
Replace the placeholder values in your code with your actual:
account_sid = "your_account_sid_here"
auth_token = "your_auth_token_here"
from_whatsapp_number = "whatsapp:+18857583493"  # Example sandbox number
to_whatsapp_number = "whatsapp:+91xxxxxxxxxx"   # Your verified number
