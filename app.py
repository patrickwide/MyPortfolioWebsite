# app.py
from flask import Flask, abort, render_template, request
import markdown
from helpers import read_json, read_markdown_file

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

blogs = 'blogs'

@app.route('/')
def index():
    return render_template('index.html', data=json_data)

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

    return render_template('success.html', data=json_data)


@app.route('/blogs')
def read_blog():
    return render_template('blogs.html', data=json_data)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
