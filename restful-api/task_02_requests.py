#!/usr/bin/python3
"""
The program will:
- Fetch and print all titles from the API response.
- Fetch and save all IDs, titles, and bodies into a CSV file.
"""
import requests  # Library to make HTTP requests
import csv  # Library to handle CSV file operations


def fetch_and_print_posts():
    """
    Fetch posts from the API and print their titles.
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))  # Print HTTP status code
    if r.status_code == 200:  # Check if request was successful
        post = r.json()  # Convert JSON response to Python object
        for data in post:  # Iterate through posts
            print(data['title'])  # Print each title


def fetch_and_save_posts():
    """
    Fetch posts from the API and save them to a CSV file.
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:  # Check if request was successful
        post = r.json()  # Convert JSON response to Python object
        # Extract id, title, and body from each post
        data = [{'id': new['id'], 'title': new['title'],
                'body': new['body']} for new in post]

        # Write data to a CSV file
        with open("posts.csv", "w") as c:
            fieldnames = ['id', 'title', 'body']  # Define CSV columns
            wry = csv.DictWriter(c, fieldnames=fieldnames)
            wry.writeheader()  # Write header row to the CSV
            wry.writerows(data)  # Write all rows to the CSV
