from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    config_value = os.getenv('APP_ENV', 'SAINATH')
    secret_value = os.getenv("APP_PASSWORD", "SAINATHSECRET")
    return f"Hello, World! Config: {config_value}, Secret: {secret_value}"
@app.route('/about')
def about():
    return "This is the about page."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)