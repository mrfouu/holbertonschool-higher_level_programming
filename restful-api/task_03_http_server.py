#!/usr/bin/python3
"""
The program will develop a simple API.
"""
import json  # Library for handling JSON data
from http.server import BaseHTTPRequestHandler, HTTPServer  # HTTP server libs


class Handler_API(BaseHTTPRequestHandler):
    """
    The class Handler_API handles HTTP GET requests.
    """
    def do_GET(self):
        # Handle the /data endpoint: return JSON with user details
        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)  # Send HTTP 200 OK
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Handle the root endpoint: return a simple text message
        elif self.path == '/':
            self.send_response(200)  # Send HTTP 200 OK
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Handle the /status endpoint: return a status message
        elif self.path == '/status':
            self.send_response(200)  # Send HTTP 200 OK
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"OK")

        # Handle the /info endpoint: return API information in JSON
        elif self.path == '/info':
            information = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)  # Send HTTP 200 OK
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(information).encode('utf-8'))

        # Handle unknown endpoints with a 404 error
        else:
            self.send_response(404)  # Send HTTP 404 Not Found
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=Handler_API, port=8000):
    """
    The function run starts the HTTP server.
    """
    server_address = ('', port)  # Bind server to all available IPs
    httpd = server_class(server_address, handler_class)  # Create server
    print("Serve on port {}...".format(port))  # Print server info
    httpd.serve_forever()  # Run the server indefinitely


if __name__ == "__main__":
    """
    Testing the class and function.
    """
    run()  # Start the server
