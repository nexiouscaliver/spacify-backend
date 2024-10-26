import sqlite3
from datetime import datetime

# waredb = "warehouse.db"
proddb = "products.db"

def create_tables():
    # Create Products table
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    cursor = c
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        category TEXT,
        client_id INTEGER NOT NULL
    );
    """)

    # Create Warehouses table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS warehouses (
        warehouse_id INTEGER PRIMARY KEY AUTOINCREMENT,
        warehouse_name TEXT NOT NULL,
        location TEXT NOT NULL,
        CAPACITY INTEGER NOT NULL DEFAULT 1000
    );
    """)

    # Create Inventory table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        warehouse_id INTEGER,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        warehouse_id INTEGER NOT NULL,
        transaction_type TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        transaction_date TEXT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS client (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL
        
    );
    """)

    conn.commit()
    conn.close()

# Function to add a new product
def add_product(name, description, price, category,client_id):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    cursor = c
    cursor.execute("""
    INSERT INTO products (product_name, description, price, category, client_id)
    VALUES (?, ?, ?, ?, ?)
    """, (name, description, price, category, client_id))
    conn.commit()
    conn.close()

# Function to add a new warehouse
def add_warehouse(name, location, capacity=1000):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    cursor = c
    cursor.execute("""
    INSERT INTO warehouses (warehouse_name, location, capacity)
    VALUES (?, ?, ?)
    """, (name, location, capacity))
    conn.commit()
    conn.close()

# Function to add inventory to a warehouse
def add_inventory(product_id, warehouse_id, quantity):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    cursor = c
    cursor.execute("""
    INSERT INTO inventory (product_id, warehouse_id, quantity)
    VALUES (?, ?, ?)
    """, (product_id, warehouse_id, quantity))
    conn.commit()
    conn.close()

# Function to update inventory quantity
def update_inventory(product_id, warehouse_id, quantity):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    cursor = c
    cursor.execute("""
    UPDATE inventory
    SET quantity = ?
    WHERE product_id = ? AND warehouse_id = ?
    """, (quantity, product_id, warehouse_id))
    conn.commit()
    conn.close()

# Function to retrieve inventory levels for a specific product across warehouses
def get_inventory_levels(product_id):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    cursor = c
    cursor.execute("""
    SELECT w.warehouse_name, i.quantity
    FROM inventory i
    JOIN warehouses w ON i.warehouse_id = w.warehouse_id
    WHERE i.product_id = ?
    """, (product_id,))
    conn.close()
    return cursor.fetchall()


# Function to retrieve all products
def get_all_products():
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    cursor = c
    cursor.execute("SELECT * FROM products")
    conn.close()
    return cursor.fetchall()

def get_warehouse():
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM warehouses")
    rows = c.fetchall()
    conn.close()
    return rows


def get_product_by_id(id):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id=?", (id,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_product_by_name(name):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE name=?", (name,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_product_by_warehouse(warehouse):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE warehouse=?", (warehouse,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_product_by_category(category):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE category=?", (category,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_product_by_price(price):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE price=?", (price,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_product_by_client_id(client_id):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE client_id=?", (client_id,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_warehouse_by_id(id):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM warehouses WHERE id=?", (id,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_warehouse_by_name(name):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM warehouses WHERE name=?", (name,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_warehouse_by_location(location):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM warehouses WHERE location=?", (location,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_inventory_by_product(product_id):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory WHERE product_id=?", (product_id,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_inventory_by_warehouse(warehouse_id):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory WHERE warehouse_id=?", (warehouse_id,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_inventory_by_product_and_warehouse(product_id, warehouse_id):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory WHERE product_id=? AND warehouse_id=?", (product_id, warehouse_id))
    rows = c.fetchall()
    conn.close()
    return rows

def get_inventory_by_quantity(quantity):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory WHERE quantity=?", (quantity,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_inventory_by_product_and_quantity(product_id, quantity):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory WHERE product_id=? AND quantity=?", (product_id, quantity))
    rows = c.fetchall()
    conn.close()
    return rows

def get_inventory_by_warehouse_and_quantity(warehouse_id, quantity):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory WHERE warehouse_id=? AND quantity=?", (warehouse_id, quantity))
    rows = c.fetchall()
    conn.close()
    return rows

def get_inventory_by_product_and_warehouse_and_quantity(product_id, warehouse_id, quantity):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory WHERE product_id=? AND warehouse_id=? AND quantity=?", (product_id, warehouse_id, quantity))
    rows = c.fetchall()
    conn.close()
    return rows

def get_warehouse_location_by_id(id):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT location FROM warehouses WHERE id=?", (id,))
    rows = c.fetchall()
    conn.close()
    return rows


#transaction functions add , sale , transfer

# Function to automatically update inventory and log transactions
def add_transaction(product_id, warehouse_id, transaction_type, quantity):
    # Check and update inventory
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    cursor = c
    cursor.execute("""
    SELECT quantity FROM inventory WHERE product_id = ? AND warehouse_id = ?
    """, (product_id, warehouse_id))
    result = cursor.fetchone()

    cursor.execute("""
    SELECT capacity FROM warehouses WHEREwarehouse_id = ?
    """, (warehouse_id))
    result2 = cursor.fetchone()

    if result:
        # Calculate new inventory quantity
        new_quantity = result[0] + quantity
        if new_quantity < 0 or new_quantity > result2[0]:
            print("Error: Not enough inventory for this operation.")
            return False  # Operation failed due to insufficient inventory

        # Update existing inventory record
        cursor.execute("""
        UPDATE inventory SET quantity = ? WHERE product_id = ? AND warehouse_id = ?
        """, (new_quantity, product_id, warehouse_id))
    else:
        # If no record exists, create a new one (only if quantity is positive)
        if quantity < 0:
            print("Error: Not enough inventory for this operation.")
            return False  # Operation failed due to insufficient inventory
        cursor.execute("""
        INSERT INTO inventory (product_id, warehouse_id, quantity)
        VALUES (?, ?, ?)
        """, (product_id, warehouse_id, quantity))

    # Log the transaction
    transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
    INSERT INTO transactions (product_id, warehouse_id, transaction_type, quantity, transaction_date)
    VALUES (?, ?, ?, ?, ?)
    """, (product_id, warehouse_id, transaction_type, quantity, transaction_date))

    conn.commit()
    conn.close()
    return True  # Operation successful

def add_sale(product_id, warehouse_id, quantity_sold):
    # Use negative quantity to represent sale (deduction)
    if add_transaction(product_id, warehouse_id, "sale", -quantity_sold):
        return(f"Sale recorded: Product ID {product_id}, Warehouse ID {warehouse_id}, Quantity Sold: {quantity_sold}")
    else:
        return("Sale transaction failed due to insufficient inventory.")

def add_transfer(product_id, source_warehouse_id, destination_warehouse_id, quantity_transferred):
    # Transfer out from source warehouse (negative quantity)
    if add_transaction(product_id, source_warehouse_id, "transfer out", -quantity_transferred):
        # Transfer in to destination warehouse (positive quantity)
        if add_transaction(product_id, destination_warehouse_id, "transfer in", quantity_transferred):
            return(f"Transfer recorded: Product ID {product_id}, From Warehouse {source_warehouse_id} to {destination_warehouse_id}, Quantity: {quantity_transferred}")
        else:
            # Rollback the initial deduction if addition to destination fails
            add_transaction(product_id, source_warehouse_id, "transfer rollback", quantity_transferred)
            return("Transfer transaction failed at destination warehouse.")
    else:
        return("Transfer transaction failed due to insufficient inventory at source warehouse.")



def get_transactions(product_id=None, warehouse_id=None, transaction_type=None, date_from=None, date_to=None,product_name=None):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    cursor = c
    query = """
    SELECT t.transaction_id, p.product_name, w.warehouse_name, t.transaction_type, t.quantity, t.transaction_date
    FROM transactions t
    JOIN products p ON t.product_id = p.product_id
    JOIN warehouses w ON t.warehouse_id = w.warehouse_id
    WHERE 1=1
    """
    params = []

    # Add filters to the query
    if product_id:
        query += " AND t.product_id = ?"
        params.append(product_id)
    if warehouse_id:
        query += " AND t.warehouse_id = ?"
        params.append(warehouse_id)
    if transaction_type:
        query += " AND t.transaction_type = ?"
        params.append(transaction_type)
    if date_from:
        query += " AND t.transaction_date >= ?"
        params.append(date_from)
    if date_to:
        query += " AND t.transaction_date <= ?"
        params.append(date_to)
    if product_name:
        query += " AND p.product_name = ?"
        params.append(product_name)

    cursor.execute(query, tuple(params))
    conn.close()
    return cursor.fetchall()

# Initialize tables
# create_tables()

