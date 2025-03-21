#!/usr/bin/python3
#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)



def file_json(filepath):
    with open(filepath, 'r') as read_json:
        data_json = json.load(read_json)
    return data_json

def file_csv(filepath):
    products = []
    with open(filepath, 'r') as read_csv:
        data_csv = csv.DictReader(read_csv)
        for row in data_csv:
            try:
                row['id'] = int(row.get('id', 0))
                row['price'] = float(row.get('price', 0.0))
            except ValueError:
                row['id'] = 0
                row['price'] = 0.0

            row['name'] = row.get('name', "N/A")
            row['category'] = row.get('category', "N/A")
            products.append(row)
    return products

def file_sql(filepath):
    con = sqlite3.connect(filepath)
    cur = con.cursor()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    cur.close()
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/items')
def items():
    with open('items.json') as j_file:
        data = json.load(j_file)
        items_list = data.get('items', [])

    return render_template('items.html', items=items_list)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    origin = request.args.get('source')
    product_id = request.args.get('id', type=int)
    if origin == "json":
        products = file_json('products.json')
    elif origin == "csv":
        products = file_csv('products.csv')
    elif origin == "sql":
        products = file_sql('products.db')
    else :
        return render_template('product_display.html', msgerror ="Wrong source")
    
    if product_id:
        products = [product for product in products if product.get("id") == product_id ]
        if not products:
            return render_template('product_display.html', msgerror ="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)