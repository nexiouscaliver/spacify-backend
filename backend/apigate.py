import os
import random
from datetime import date as dt
from datetime import datetime
from datetime import timedelta
import threading
from flask import *
from flask import jsonify, request, send_from_directory
# from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from logging.config import dictConfig
from subprocess import run
import dbserver as db         #FOR SQL SERVER DATABASE
import loginscript as login   #FOR SQL SERVER DATABASE
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key =  "spacIFY_792739"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'down_files')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
TEMP_FOLDER = os.path.join(APP_ROOT, 'temp_files')
app.config['TEMP_FOLDER'] = TEMP_FOLDER
app.config['SECRET_KEY'] = "spacIFY_792739"

@app.route('/')
def home():
    #return redirect(url_for('intro'))
    return jsonify("ERROR : contact the correct endpoint for the API"), 404

@app.route('/api/v1/warelogin',methods=['POST'])
def warelogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login.load_ware(username,password):
            return jsonify("Login Successfull"), 200
        else:
            return jsonify("Login Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

@app.route('/api/v1/warecreate',methods=['POST'])
def warecreate():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        if login.create_ware(username,password,name):
            return jsonify("Account Created"), 200
        else:
            return jsonify("Account Creation Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

@app.route('/api/v1/clientlogin',methods=['POST'])
def clientlogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login.load_client(username,password):
            return jsonify("Login Successfull"), 200
        else:
            return jsonify("Login Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

@app.route('/api/v1/clientcreate',methods=['POST'])
def clientcreate():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        if login.create_client(username,password,name):
            return jsonify("Account Created"), 200
        else:
            return jsonify("Account Creation Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

#dbroutes

# Function to add a new product
@app.route('/api/v1/addproduct',methods=['POST'])
def addproduct():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        category = request.form['category']
        clientid = login.getid_client(request.form['client'])

        if db.add_product(name, description, price, category, clientid):
            return jsonify("Product Added"), 200
        else:
            return jsonify("Product Addition Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

# Function to add a new warehouse
@app.route('/api/v1/addwarehouse',methods=['POST'])
def addwarehouse():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        quantity = request.form['quantity']
        if db.add_warehouse(name, location, quantity):
            return jsonify("Warehouse Added"), 200
        else:
            return jsonify("Warehouse Addition Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

# Function to add a new inventory
@app.route('/api/v1/addinventory',methods=['POST'])
def addinventory():
    if request.method == 'POST':
        product_id = request.form['product_id']
        warehouse_id = request.form['warehouse_id']
        quantity = request.form['quantity']
        if db.add_inventory(product_id, warehouse_id, quantity):
            return jsonify("Inventory Added"), 200
        else:
            return jsonify("Inventory Addition Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

# Function to get all products
@app.route('/api/v1/getallproducts',methods=['GET'])
def getallproducts():
    if request.method == 'GET':
        products = db.get_all_products()
        return jsonify(products), 200
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

# Function to get all warehouses
@app.route('/api/v1/getwarehouses',methods=['GET'])
def getwarehouses():
    if request.method == 'GET':
        warehouses = db.get_warehouse()
        return jsonify(warehouses), 200
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404



# Function to update inventory quantity
@app.route('/api/v1/updateinventory',methods=['POST'])
def updateinventory():
    if request.method == 'POST':
        product_id = request.form['product_id']
        warehouse_id = request.form['warehouse_id']
        quantity = request.form['quantity']
        if db.update_inventory(product_id, warehouse_id, quantity):
            return jsonify("Inventory Updated"), 200
        else:
            return jsonify("Inventory Update Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

# Function to retrieve inventory levels for a specific product across warehouses
@app.route('/api/v1/getinventorylevels',methods=['GET'])
def getinventorylevels():
    if request.method == 'GET':
        product_id = request.form['product_id']
        inventory = db.get_inventory_levels(product_id)
        return jsonify(inventory), 200
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

@app.route('/api/v1/get_product_by_id', methods=['GET'])
def get_product_by_id():
    id = request.args.get('id')
    product = db.get_product_by_id(id)
    return jsonify(product) if product else jsonify("Product not found"), 404

@app.route('/api/v1/get_product_by_name', methods=['GET'])
def get_product_by_name():
    name = request.args.get('name')
    product = db.get_product_by_name(name)
    return jsonify(product) if product else jsonify("Product not found"), 404

@app.route('/api/v1/get_product_by_warehouse', methods=['GET'])
def get_product_by_warehouse():
    warehouse = request.args.get('warehouse')
    product = db.get_product_by_warehouse(warehouse)
    return jsonify(product) if product else jsonify("Product not found"), 404

@app.route('/api/v1/get_product_by_category', methods=['GET'])
def get_product_by_category():
    category = request.args.get('category')
    product = db.get_product_by_category(category)
    return jsonify(product) if product else jsonify("Product not found"), 404

@app.route('/api/v1/get_product_by_price', methods=['GET'])
def get_product_by_price():
    price = request.args.get('price')
    product = db.get_product_by_price(price)
    return jsonify(product) if product else jsonify("Product not found"), 404

@app.route('/api/v1/get_product_by_client_id', methods=['GET'])
def get_product_by_client_id():
    client_id = request.args.get('client_id')
    product = db.get_product_by_client_id(client_id )
    return jsonify(product) if product else jsonify("Product not found"), 404

# Routes for getting warehouse information
@app.route('/api/v1/get_warehouse_by_id', methods=['GET'])
def get_warehouse_by_id():
    id = request.args.get('id')
    warehouse = db.get_warehouse_by_id(id)
    return jsonify(warehouse) if warehouse else jsonify("Warehouse not found"), 404

@app.route('/api/v1/get_warehouse_by_name', methods=['GET'])
def get_warehouse_by_name():
    name = request.args.get('name')
    warehouse = db.get_warehouse_by_name(name)
    return jsonify(warehouse) if warehouse else jsonify("Warehouse not found"), 404

@app.route('/api/v1/get_warehouse_by_location', methods=['GET'])
def get_warehouse_by_location():
    location = request.args.get('location')
    warehouse = db.get_warehouse_by_location(location)
    return jsonify(warehouse) if warehouse else jsonify("Warehouse not found"), 404

# Routes for getting inventory information
@app.route('/api/v1/get_inventory_by_product', methods=['GET'])
def get_inventory_by_product():
    product_id = request.args.get('product_id')
    inventory = db.get_inventory_by_product(product_id)
    return jsonify(inventory) if inventory else jsonify("Inventory not found"), 404

@app.route('/api/v1/get_inventory_by_warehouse', methods=['GET'])
def get_inventory_by_warehouse():
    warehouse_id = request.args.get('warehouse_id')
    inventory = db.get_inventory_by_warehouse(warehouse_id)
    return jsonify(inventory) if inventory else jsonify("Inventory not found"), 404

@app.route('/api/v1/get_inventory_by_product_and_warehouse', methods=['GET'])
def get_inventory_by_product_and_warehouse():
    product_id = request.args.get('product_id')
    warehouse_id = request.args.get('warehouse_id')
    inventory = db.get_inventory_by_product_and_warehouse(product_id, warehouse_id)
    return jsonify(inventory) if inventory else jsonify("Inventory not found"), 404

@app.route('/api/v1/get_inventory_by_quantity', methods=['GET'])
def get_inventory_by_quantity():
    quantity = request.args.get('quantity')
    inventory = db.get_inventory_by_quantity(quantity)
    return jsonify(inventory) if inventory else jsonify("Inventory not found"), 404

@app.route('/api/v1/get_inventory_by_product_and_quantity', methods=['GET'])
def get_inventory_by_product_and_quantity():
    product_id = request.args.get('product_id')
    quantity = request.args.get('quantity')
    inventory = db.get_inventory_by_product_and_quantity(product_id, quantity)
    return jsonify(inventory) if inventory else jsonify("Inventory not found"), 404

@app.route('/api/v1/get_inventory_by_warehouse_and_quantity', methods=['GET'])
def get_inventory_by_warehouse_and_quantity():
    warehouse_id = request.args.get('warehouse_id')
    quantity = request.args.get('quantity')
    inventory = db.get_inventory_by_warehouse_and_quantity(warehouse_id, quantity)
    return jsonify(inventory) if inventory else jsonify("Inventory not found"), 404

@app.route('/api/v1/get_inventory_by_product_and_warehouse_and_quantity', methods=['GET'])
def get_inventory_by_product_and_warehouse_and_quantity():
    product_id = request.args.get('product_id')
    warehouse_id = request.args.get('warehouse_id')
    quantity = request.args.get('quantity')
    inventory = db.get_inventory_by_product_and_warehouse_and_quantity(product_id, warehouse_id, quantity)
    return jsonify(inventory) if inventory else jsonify("Inventory not found"), 404

@app.route('/api/v1/get_warehouse_location_by_id', methods=['GET'])
def get_warehouse_location_by_id():
    id = request.args.get('id')
    location = db.get_warehouse_location_by_id(id)
    return jsonify(location) if location else jsonify("Location not found"), 404

# Routes for adding transactions
@app.route('/api/v1/add_transaction', methods=['POST'])
def add_transaction():
    data = request.form
    product_id = data.get('product_id')
    warehouse_id = data.get('warehouse_id')
    transaction_type = data.get('transaction_type')
    quantity = data.get('quantity')
    if db.add_transaction(product_id, warehouse_id, transaction_type, quantity):
        return jsonify("Transaction added"), 200
    else:
        return jsonify("Transaction addition failed"), 404

@app.route('/api/v1/add_sale', methods=['POST'])
def add_sale():
    data = request.form
    product_id = data.get('product_id')
    warehouse_id = data.get('warehouse_id')
    quantity_sold = data.get('quantity_sold')
    if db.add_sale(product_id, warehouse_id, quantity_sold):
        return jsonify("Sale added"), 200
    else:
        return jsonify("Sale addition failed"), 404

@app.route('/api/v1/add_transfer', methods=['POST'])
def add_transfer():
    data = request.form
    product_id = data.get('product_id')
    source_warehouse_id = data.get('source_warehouse_id')
    destination_warehouse_id = data.get('destination_warehouse_id')
    quantity_transferred = data.get('quantity_transferred')
    if db.add_transfer(product_id, source_warehouse_id, destination_warehouse_id, quantity_transferred):
        return jsonify("Transfer added"), 200
    else:
        return jsonify("Transfer addition failed"), 404

# Route for getting transactions
@app.route('/api/v1/get_transactions', methods=['GET'])
def get_transactions():
    product_id = request.args.get('product_id')
    warehouse_id = request.args.get('warehouse_id')
    transaction_type = request.args.get('transaction_type')
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    product_name = request.args.get('product_name')
    transactions = db.get_transactions(product_id, warehouse_id, transaction_type, date_from, date_to, product_name)
    return jsonify(transactions) if transactions else jsonify("Transactions not found"), 404




# running the app
if __name__ == '__main__':
    app.run(debug=True)
