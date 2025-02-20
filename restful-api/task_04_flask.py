#!/usr/bin/python3
"""
The program will develop a simple API with Flask.
"""

from flask import Flask, jsonify, request
# Import Flask and helpers

app = Flask(__name__)  # Create the Flask app
users = {}  # Dictionary to store user data


@app.route("/")
def home():
    """
    Root endpoint to welcome users.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def GU():
    """
    Endpoint to get a list of all usernames.
    """
    return jsonify(list(users.keys()))  # Return all usernames


@app.route('/status')
def stat():
    """
    Endpoint to check the API status.
    """
    return "OK"  # Return a simple status message


@app.route('/users/<username>')
def search_user(username):
    """
    Endpoint to search for a user by username.
    """
    user = users.get(username)  # Retrieve user data from dictionary
    if user:
        return jsonify(user)  # Return user data if found
    else:
        return jsonify({"error": "User not found"}), 404  # Return error


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a new user via POST request.
    """
    data = request.get_json()  # Parse JSON payload from the request
    new = data.get('username')  # Get the 'username' field

    if new:  # Check if 'username' is provided
        users[new] = data  # Add user data to the dictionary
        return jsonify({"message": "User added", "user": data}), 201
    else:
        return jsonify({"error": "Username is required"}), 400
    # Error if missing


if __name__ == "__main__":
    """
    Run the Flask app.
    """
    app.run()  # Start the Flask application
