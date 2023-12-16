import json
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Load environment variables from a .env file
load_dotenv()

def read_json(file_name):
    # Get the absolute path to the JSON file
    my_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(my_dir, file_name)

    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
        return data # return the Python dictionary
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

def send_emails(receiver_emails, subjects, bodies):
    try:
        # Use environment variables for sensitive information
        password = os.getenv("EMAIL_PASSWORD")
        app_email = os.getenv("APP_EMAIL")

        # Connect to the SMTP server (for Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(app_email, password)

        for receiver_email, subject, body in zip(receiver_emails, subjects, bodies):
            # Create message
            message = MIMEMultipart()
            message['From'] = app_email
            message['To'] = receiver_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Send email
            server.sendmail(app_email, receiver_email, message.as_string())

        # Quit the server
        server.quit()

        print("Emails sent successfully.")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False


