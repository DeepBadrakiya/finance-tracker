#!/usr/bin/env python3
"""General Store Web Application - Simplified Version"""

import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'store_secret_key_2026'

# Sample products
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics", "stock": 15},
    {"id": 2, "name": "Wireless Mouse", "price": 29.99, "category": "Electronics", "stock": 50},
    {"id": 3, "name": "USB-C Cable", "price": 15.99, "category": "Electronics", "stock": 100},
    {"id": 4, "name": "Coffee Maker", "price": 89.99, "category": "Appliances", "stock": 20},
    {"id": 5, "name": "Blender", "price": 49.99, "category": "Appliances", "stock": 25},
    {"id": 6, "name": "Toaster", "price": 34.99, "category": "Appliances", "stock": 30},
    {"id": 7, "name": "Desk Lamp", "price": 39.99, "category": "Office", "stock": 40},
    {"id": 8, "name": "Office Chair", "price": 199.99, "category": "Office", "stock": 12},
    {"id": 9, "name": "Bookshelf", "price": 129.99, "category": "Furniture", "stock": 8},
    {"id": 10, "name": "Wall Clock", "price": 24.99, "category": "Decor", "stock": 35},
]

def load_orders():
    """Load orders from file"""
    if os.path.exists('store_data.json'):
        try:
            with open('store_data.json', 'r') as f:
                return json.load(f)
        except:
            return {"orders": []}
    return {"orders": []}

def save_orders(data):
    """Save orders to file"""
    with open('store_data.json', 'w') as f:
        json.dump(data, f, indent=2)

# Routes
@app.route('/')
def index():
    """Home page"""
    return render_template('index.html', products_count=len(PRODUCTS))

@app.route('/products')
def products():
    """Products page"""
    category = request.args.get('category', 'all')
    
    if category == 'all':
        filtered = PRODUCTS
    else:
        filtered = [p for p in PRODUCTS if p['category'].lower() == category.lower()]
    
    categories = sorted(list(set(p['category'] for p in PRODUCTS)))
    return render_template('products.html', products=filtered, categories=categories, current_category=category)

@app.route('/product/<int:pid>')
def product_detail(pid):
    """Product detail page"""
    product = next((p for p in PRODUCTS if p['id'] == pid), None)
    if not product:
        return render_template('404.html'), 404
    return render_template('product_detail.html', product=product)

@app.route('/cart')
def cart():
    """Shopping cart page"""
    cart_items = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/orders')
def orders():
    """Orders page"""
    orders_data = load_orders()
    return render_template('orders.html', orders=orders_data.get('orders', []))

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

# API Routes
@app.route('/api/add-to-cart', methods=['POST'])
def add_to_cart():
    """Add item to cart"""
    data = request.get_json()
    product_id = int(data.get('product_id'))
    quantity = int(data.get('quantity', 1))
    
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return jsonify({"success": False, "message": "Product not found"}), 400
    
    if quantity > product['stock']:
        return jsonify({"success": False, "message": "Insufficient stock"}), 400
    
    cart = session.get('cart', [])
    existing = next((item for item in cart if item['id'] == product_id), None)
    
    if existing:
        existing['quantity'] += quantity
    else:
        cart.append({
            'id': product_id,
            'name': product['name'],
            'price': product['price'],
            'quantity': quantity
        })
    
    session['cart'] = cart
    session.modified = True
    cart_count = sum(item['quantity'] for item in cart)
    
    return jsonify({"success": True, "cart_count": cart_count})

@app.route('/api/remove-from-cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    """Remove item from cart"""
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]
    session['cart'] = cart
    session.modified = True
    cart_count = sum(item['quantity'] for item in cart)
    
    return jsonify({"success": True, "cart_count": cart_count})

@app.route('/api/checkout', methods=['POST'])
def checkout():
    """Process checkout"""
    cart = session.get('cart', [])
    if not cart:
        return jsonify({"success": False, "message": "Cart is empty"}), 400
    
    data = request.get_json()
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
    
    return jsonify({"success": True, "order_id": order["order_id"]})

# Error handlers
@app.errorhandler(404)
def not_found(e):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    """500 error handler"""
    print(f"Server error: {e}")
    return render_template('404.html'), 500

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 GENERAL STORE WEB APPLICATION")
    print("="*50)
    print("📍 Opening: http://localhost:5000")
    print("⚠️  Press Ctrl+C to stop")
    print("="*50 + "\n")
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
