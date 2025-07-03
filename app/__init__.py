# app.py
from flask import Flask

# Create app instance
app = Flask(__name__)

# Avoid circular import by not importing app in the same file
if __name__ == '__main__':
    app.run(debug=True)
