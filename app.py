# app.py
from flask import Flask, render_template, request
from helpers import read_json, send_emails

from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Configure the path to the templates and static directories
app.template_folder = 'templates'
app.static_folder = 'static'

app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)

# My Data:
file_path = 'data.json'
json_data = read_json(file_path)

@app.route('/')
def index():
    # Check if data is retrieved successfully
    if json_data is not None:
        # Render the template with the JSON data
        return render_template('index.html', data=json_data)
    else:
        # Return an error message if the file is not found or returns None
        return "Error: Unable to retrieve JSON data. Check if the file exists."

@app.route('/contact', methods=['GET', 'POST'])
def process_form():
    if request.method == 'POST':
        # Handle form submission here
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Assuming json_data is loaded from a JSON file
        try:
            # Load your JSON data here
            # json_data = ...

            receiver_emails = [email, json_data['contact']['form']['notification_email']['receiver_email']]
            subjects = [json_data['contact']['form']['confirmation_email']['subject'], json_data['contact']['form']['notification_email']['subject']]
            
            notification_body = f"{json_data['contact']['form']['notification_email']['body']}\n\n\nName: {name}\nEmail: {email}\nMessage: {message}"
            bodies = [json_data['contact']['form']['confirmation_email']['body'], notification_body]

            # Attempt to send emails
            if send_emails(receiver_emails, subjects, bodies):
                success_message = "Success: Your email has been sent successfully. Thank you for contacting us!"
                return render_template('success.html', data=json_data, success_message=success_message)
            else:
                # If sending emails fails, provide an error message
                error_message = f"Error: Unable to send emails. Please try again later or contact us directly at {json_data['contact']['form']['notification_email']['subject']}"
                return render_template('error.html', error_message=error_message)
        except Exception as e:
            # Handle exceptions related to JSON loading or any other unexpected issues
            return f"Error: {str(e)}"
    
    return "Error: This route only supports POST requests."

@app.route('/blogs')
def read_blog():
    if json_data is not None:
        return render_template('blogs.html', data=json_data)
    else:
        # Return an error message if the file is not found or returns None
        return "Error: Unable to retrieve JSON data. Check if the file exists."


if __name__ == '__main__':
    app.run(debug=True, port=5002)
