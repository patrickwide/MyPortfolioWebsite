# Portfolio Website with Flask and Tailwind CSS

This project is a simple portfolio website built using Flask, a Python web framework, and Tailwind CSS for styling. The website is designed to be easily customizable by anyone who wants to showcase their portfolio. It uses a simple JSON file to store user data, making it easy to host and run as a normal Flask application.

## Features

- **Homepage**: Display your portfolio items on the homepage.
- **Contact Page**: Allow visitors to contact you through a form.
- **Blogs Page**: Showcase your blogs.

## Prerequisites

Make sure you have the following installed:

- Python (version 3.x)
- Flask
- Flask-WTF
- Tailwind CSS

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/patrickwide/MyPortfolioWebsite.git
   cd MyPortfolioWebsite/
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

   The application will be accessible at `http://localhost:5001` by default.

# Configuration

- Update the `data.json` file with your own information.
- Customize the templates in the `templates` folder to match your style.
- Set up your email app password to enable the contact form functionality.

## Environment Variables

Create a `.env` file in the root directory of your project and add the following variables in the specified format:

```dotenv
# .env file

# Set your email app password in the following format
EMAIL_PASSWORD=your_email_app_password

# Provide your app email (if applicable)
APP_EMAIL=your_app_email

# Specify your personal email for receiving contact form submissions
YOUR_EMAIL=your_personal_email@example.com
```

## How to Use

- Access the homepage at `/` to view your portfolio.
- Visit the contact page at `/contact` to allow visitors to contact you.
- Check out your blogs at `/blogs`.

## Contributing

Feel free to contribute by opening issues or creating pull requests. Your feedback and improvements are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
