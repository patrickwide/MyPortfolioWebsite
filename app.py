# app.py
from flask import Flask, render_template, request
from helpers import read_json

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
        # Process data as needed (e.g., send email, save to database)
        print(name)
        print(email)
        print(message)
    if json_data is not None:
        return render_template('success.html', data=json_data)
    else:
        # Return an error message if the file is not found or returns None
        return "Error: Unable to retrieve JSON data. Check if the file exists."
        
@app.route('/blogs')
def read_blog():
    if json_data is not None:
        return render_template('blogs.html', data=json_data)
    else:
        # Return an error message if the file is not found or returns None
        return "Error: Unable to retrieve JSON data. Check if the file exists."


if __name__ == '__main__':
    app.run(debug=True, port=5002)
