import json
import os

def read_json(file_path):
    # Read data from the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def read_markdown_file(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        return f.read()

import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Load environment variables from a .env file
load_dotenv()

def send_emails(sender_email, receiver_emails, subjects, bodies):
    try:
        # Use environment variables for sensitive information
        password = os.getenv("EMAIL_PASSWORD")

        # Connect to the SMTP server (for Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        for receiver_email, subject, body in zip(receiver_emails, subjects, bodies):
            # Create message
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Send email
            server.sendmail(sender_email, receiver_email, message.as_string())

        # Quit the server
        server.quit()

        print("Emails sent successfully.")
    except Exception as e:
        print(f"Error: {e}")

# # Example usage:
# sender_email = 'patrickwide.com@gmail.com'
# receiver_emails = ['patrickwide254@gmail.com', 'patpal911@gmail.com']
# subjects = ['Subject of Email 1', 'Subject of Email 2']
# bodies = ['Body of Email 1', 'Body of Email 2']
# send_emails(sender_email, receiver_emails, subjects, bodies)

