import json
import pathlib

def read_json(file_name):
    # Get the absolute path to the JSON file
    json_file_path = pathlib.Path(file_name).absolute()

    # Check if the file exists
    if json_file_path.exists():
        # Read data from the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        return data
    else:
        print(f"The file '{json_file_path}' does not exist.")
        return None

# import os
# from dotenv import load_dotenv
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib

# # Load environment variables from a .env file
# load_dotenv()

# def send_emails(sender_email, receiver_emails, subjects, bodies):
#     try:
#         # Use environment variables for sensitive information
#         password = os.getenv("EMAIL_PASSWORD")

#         # Connect to the SMTP server (for Gmail)
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(sender_email, password)

#         for receiver_email, subject, body in zip(receiver_emails, subjects, bodies):
#             # Create message
#             message = MIMEMultipart()
#             message['From'] = sender_email
#             message['To'] = receiver_email
#             message['Subject'] = subject
#             message.attach(MIMEText(body, 'plain'))

#             # Send email
#             server.sendmail(sender_email, receiver_email, message.as_string())

#         # Quit the server
#         server.quit()

#         print("Emails sent successfully.")
#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage:
# sender_email = 'patrickwide.com@gmail.com'
# receiver_emails = ['patrickwide254@gmail.com', 'patpal911@gmail.com']
# subjects = ['Subject of Email 1', 'Subject of Email 2']
# bodies = ['Body of Email 1', 'Body of Email 2']
# send_emails(sender_email, receiver_emails, subjects, bodies)

