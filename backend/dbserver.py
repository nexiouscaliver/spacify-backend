import sqlite3

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
        category TEXT
    );
    """)

    # Create Warehouses table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS warehouses (
        warehouse_id INTEGER PRIMARY KEY AUTOINCREMENT,
        warehouse_name TEXT NOT NULL,
        location TEXT NOT NULL
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

    conn.commit()
    conn.close()

# Function to add a new product
def add_product(name, description, price, category):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    cursor = c
    cursor.execute("""
    INSERT INTO products (product_name, description, price, category)
    VALUES (?, ?, ?, ?)
    """, (name, description, price, category))
    conn.commit()
    conn.close()

# Function to add a new warehouse
def add_warehouse(name, location):
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    cursor = c
    cursor.execute("""
    INSERT INTO warehouses (warehouse_name, location)
    VALUES (?, ?)
    """, (name, location))
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

def get_product():
    conn = sqlite3.connect(proddb)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
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
