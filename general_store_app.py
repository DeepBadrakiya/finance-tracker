#!/usr/bin/env python3
"""General Store Web Application using Flask."""

import os
import sys
import json
from datetime import datetime

# Suppress deprecation warnings for Python 3.14 compatibility
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'
app.config['JSON_SORT_KEYS'] = False

# Sample product database
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics", "image": "laptop.jpg", "stock": 15},
    {"id": 2, "name": "Wireless Mouse", "price": 29.99, "category": "Electronics", "image": "mouse.jpg", "stock": 50},
    {"id": 3, "name": "USB-C Cable", "price": 15.99, "category": "Electronics", "image": "cable.jpg", "stock": 100},
    {"id": 4, "name": "Coffee Maker", "price": 89.99, "category": "Appliances", "image": "coffee.jpg", "stock": 20},
    {"id": 5, "name": "Blender", "price": 49.99, "category": "Appliances", "image": "blender.jpg", "stock": 25},
    {"id": 6, "name": "Toaster", "price": 34.99, "category": "Appliances", "image": "toaster.jpg", "stock": 30},
    {"id": 7, "name": "Desk Lamp", "price": 39.99, "category": "Office", "image": "lamp.jpg", "stock": 40},
    {"id": 8, "name": "Office Chair", "price": 199.99, "category": "Office", "image": "chair.jpg", "stock": 12},
    {"id": 9, "name": "Bookshelf", "price": 129.99, "category": "Furniture", "image": "shelf.jpg", "stock": 8},
    {"id": 10, "name": "Wall Clock", "price": 24.99, "category": "Decor", "image": "clock.jpg", "stock": 35},
]

DATA_FILE = "store_data.json"

def load_orders():
    """Load orders from file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"orders": []}

def save_orders(data):
    """Save orders to file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    """Home page."""
    return render_template('index.html', products_count=len(PRODUCTS))

@app.route('/products')
def products():
    """Show all products."""
    category = request.args.get('category', 'all')
    
    if category == 'all':
        filtered_products = PRODUCTS
    else:
        filtered_products = [p for p in PRODUCTS if p['category'].lower() == category.lower()]
    
    categories = list(set(p['category'] for p in PRODUCTS))
    return render_template('products.html', products=filtered_products, categories=categories, current_category=category)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """Show product details."""
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return render_template('404.html'), 404
    return render_template('product_detail.html', product=product)

@app.route('/cart')
def cart():
    """Show shopping cart."""
    cart_items = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/api/add-to-cart', methods=['POST'])
def add_to_cart():
    """Add item to cart (API endpoint)."""
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product or quantity > product['stock']:
        return jsonify({"success": False, "message": "Invalid product or insufficient stock"}), 400
    
    cart = session.get('cart', [])
    
    # Check if product already in cart
    existing_item = next((item for item in cart if item['id'] == product_id), None)
    if existing_item:
        existing_item['quantity'] += quantity
    else:
        cart.append({
            'id': product_id,
            'name': product['name'],
            'price': product['price'],
            'quantity': quantity
        })
    
    session['cart'] = cart
    session.modified = True
    
    return jsonify({"success": True, "message": "Added to cart", "cart_count": sum(item['quantity'] for item in cart)})

@app.route('/api/remove-from-cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    """Remove item from cart."""
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]
    session['cart'] = cart
    session.modified = True
    
    return jsonify({"success": True, "message": "Removed from cart", "cart_count": sum(item['quantity'] for item in cart)})

@app.route('/api/checkout', methods=['POST'])
def checkout():
    """Process checkout."""
    cart = session.get('cart', [])
    if not cart:
        return jsonify({"success": False, "message": "Cart is empty"}), 400
    
    data = request.json
    order = {
        "order_id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "customer_name": data.get('name'),
        "customer_email": data.get('email'),
        "customer_address": data.get('address'),
        "items": cart,
        "total": sum(item['price'] * item['quantity'] for item in cart),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Confirmed"
    }
    
    store_data = load_orders()
    store_data["orders"].append(order)
    save_orders(store_data)
    
    session['cart'] = []
    session.modified = True
    
    return jsonify({"success": True, "message": "Order placed successfully!", "order_id": order["order_id"]})

@app.route('/orders')
def orders():
    """Show all orders."""
    store_data = load_orders()
    return render_template('orders.html', orders=store_data.get('orders', []))

@app.route('/about')
def about():
    """About page."""
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    print("🚀 Starting General Store Web Application...")
    print("📍 Open your browser: http://localhost:5000")
    print("⚠️  Press Ctrl+C to stop the server")
    try:
        app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
    except KeyboardInterrupt:
        print("\n👋 Server stopped!")
        sys.exit(0)
