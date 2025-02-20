#!/usr/bin/python3
"""
The program will develop a Flask API with:
- Security
- Authentication using Basic Auth and JWT
"""

from flask import Flask, jsonify, request  # Flask utilities
from flask_httpauth import HTTPBasicAuth  # Basic authentication
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
auth = HTTPBasicAuth()  # Initialize Basic Authentication
app.config['JWT_SECRET_KEY'] = 'secret_key'  # Secret key for JWT
jwt = JWTManager(app)  # Initialize JWT Manager

# Dictionary to store user data with hashed passwords
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify username and password for Basic Authentication.
    """
    User = users.get(username)
    if User and check_password_hash(User["password"], password):
        return username  # Return username if authentication succeeds
    return None


@app.route("/")
def home():
    """
    Root endpoint for API.
    """
    return "Welcome to the Flask API!"


@app.route("/login", methods=['POST'])
def login():
    """
    Endpoint for user login to generate a JWT token.
    """
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    cur_user = users.get(username)
    if cur_user and check_password_hash(cur_user['password'], password):
        token = create_access_token(identity=username)  # Generate JWT token
        return jsonify(access_token=token), 200
    return jsonify({"message": "Bad username or password"}), 401


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Endpoint protected by Basic Authentication.
    """
    return "Basic Auth: Access Granted"


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Endpoint protected by JWT Authentication.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin():
    """
    Endpoint accessible only to admin users via JWT Authentication.
    """
    cur_user = get_jwt_identity()  # Get current user's identity
    user = users.get(cur_user)

    if user['role'] == "admin":  # Check if the user has admin role
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403


# Error handling for various JWT-related issues
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing or invalid tokens.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid token errors.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired tokens.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked tokens.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle cases where a fresh token is required.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    """
    Run the Flask application.
    """
    app.run()
