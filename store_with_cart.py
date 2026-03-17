#!/usr/bin/env python3
"""General Store - Complete Working Version with Cart"""
import flask
import sys
import json

app = flask.Flask(__name__)
app.secret_key = 'general_store_secret_key_2026'

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics"},
    {"id": 2, "name": "Wireless Mouse", "price": 29.99, "category": "Electronics"},
    {"id": 3, "name": "USB-C Cable", "price": 15.99, "category": "Electronics"},
    {"id": 4, "name": "Coffee Maker", "price": 89.99, "category": "Appliances"},
    {"id": 5, "name": "Blender", "price": 49.99, "category": "Appliances"},
    {"id": 6, "name": "Toaster", "price": 34.99, "category": "Appliances"},
]

HTML_HOME = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>General Store</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<style>
body { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; min-height: 100vh; display: flex; align-items: center; }
.container { text-align: center; }
h1 { font-size: 3.5rem; margin-bottom: 20px; }
.lead { font-size: 1.3rem; margin-bottom: 40px; }
.btn-light { padding: 15px 40px; font-size: 1.1rem; font-weight: bold; }
</style>
</head>
<body>
<div class="container">
<h1>🛍️ General Store</h1>
<p class="lead">Welcome! Your one-stop shop for quality products</p>
<a href="/products" class="btn btn-light btn-lg">🛒 Shop Now</a>
</div>
</body>
</html>"""

HTML_PRODUCTS = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Products - General Store</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<style>
body { background: #f5f5f5; }
.navbar { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important; }
.card { box-shadow: 0 4px 15px rgba(0,0,0,0.2); border: none; transition: transform 0.3s, box-shadow 0.3s; }
.card:hover { transform: translateY(-10px); box-shadow: 0 8px 25px rgba(0,0,0,0.3); }
.price { color: #667eea; font-size: 1.8rem; font-weight: bold; }
.btn-primary { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border: none; }
.btn-primary:hover { background: linear-gradient(135deg, #764ba2 0%, #667eea 100%); }
.badge-cart { background: #dc3545; border-radius: 50%; width: 25px; height: 25px; display: flex; align-items: center; justify-content: center; }
</style>
</head>
<body>
<nav class="navbar navbar-dark">
<div class="container-fluid">
<span class="navbar-brand fs-4 fw-bold">🛍️ General Store</span>
<div>
<a href="/cart" class="btn btn-light btn-sm me-2"><i class="fas fa-shopping-cart"></i> Cart <span class="badge-cart" id="cart-count">0</span></a>
<a href="/" class="btn btn-light btn-sm">← Home</a>
</div>
</div>
</nav>
<div class="container py-5">
<h2 class="mb-5">Our Featured Products</h2>
<div class="row">
""" + "".join([f"""
<div class="col-md-4 mb-4">
<div class="card h-100">
<div class="card-body text-center">
<h5 class="card-title">{p['name']}</h5>
<p class="price">${p['price']:.2f}</p>
<p class="text-muted mb-3">{p['category']}</p>
<button class="btn btn-primary w-100" onclick="addToCart({p['id']}, '{p['name']}', {p['price']})">
<i class="fas fa-plus"></i> Add to Cart
</button>
</div>
</div>
</div>
""" for p in PRODUCTS]) + """
</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script>
function addToCart(id, name, price) {
    fetch('/api/add-to-cart', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id: id, name: name, price: price, quantity: 1})
    })
    .then(r => r.json())
    .then(data => {
        document.getElementById('cart-count').textContent = data.cart_count;
        alert('✅ ' + name + ' added to cart!');
    })
    .catch(e => alert('Error: ' + e));
}
window.addEventListener('load', function() {
    fetch('/api/get-cart-count')
    .then(r => r.json())
    .then(data => {
        document.getElementById('cart-count').textContent = data.count;
    });
});
</script>
</body>
</html>"""

HTML_CART = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Shopping Cart - General Store</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<style>
body { background: #f5f5f5; }
.navbar { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important; }
.btn-primary { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border: none; }
.btn-primary:hover { background: linear-gradient(135deg, #764ba2 0%, #667eea 100%); }
.total-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 10px; }
</style>
</head>
<body>
<nav class="navbar navbar-dark">
<div class="container-fluid">
<span class="navbar-brand fs-4 fw-bold">🛍️ General Store</span>
<div>
<a href="/products" class="btn btn-light btn-sm">← Continue Shopping</a>
</div>
</div>
</nav>
<div class="container py-5">
<h2 class="mb-4"><i class="fas fa-shopping-cart"></i> Your Shopping Cart</h2>

{cart_html}

</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script>
function removeFromCart(itemId) {
    if (confirm('Remove this item?')) {
        fetch('/api/remove-from-cart', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({id: itemId})
        })
        .then(r => r.json())
        .then(data => {
            location.reload();
        });
    }
}
function checkout() {
    alert('✅ Order placed! Thank you for shopping!');
    fetch('/api/checkout', {method: 'POST'})
    .then(r => location.href = '/');
}
</script>
</body>
</html>"""

EMPTY_CART = """
<div class="alert alert-info text-center py-5">
<i class="fas fa-shopping-cart fa-5x mb-3"></i>
<p class="lead">Your cart is empty</p>
<a href="/products" class="btn btn-primary">Continue Shopping</a>
</div>
"""

@app.route("/", methods=["GET"])
def home():
    return HTML_HOME, 200, {"Content-Type": "text/html; charset=utf-8"}

@app.route("/products", methods=["GET"])  
def products():
    return HTML_PRODUCTS, 200, {"Content-Type": "text/html; charset=utf-8"}

@app.route("/cart", methods=["GET"])
def cart():
    cart_items = flask.session.get('cart', [])
    
    if not cart_items:
        cart_html = EMPTY_CART
    else:
        total = sum(item['price'] * item['quantity'] for item in cart_items)
        rows = "".join([f"""
        <tr>
            <td>{item['name']}</td>
            <td>${item['price']:.2f}</td>
            <td>{item['quantity']}</td>
            <td>${item['price'] * item['quantity']:.2f}</td>
            <td><button class="btn btn-danger btn-sm" onclick="removeFromCart({item['id']})"><i class="fas fa-trash"></i></button></td>
        </tr>
        """ for item in cart_items])
        
        cart_html = f"""
        <div class="row">
            <div class="col-lg-8">
                <table class="table table-hover">
                    <thead class="table-light">
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Qty</th>
                            <th>Total</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows}
                    </tbody>
                </table>
            </div>
            <div class="col-lg-4">
                <div class="total-box">
                    <h5>Order Summary</h5>
                    <hr style="border-color: rgba(255,255,255,0.3);">
                    <p>Subtotal: <strong>${total:.2f}</strong></p>
                    <p>Shipping: <strong>FREE</strong></p>
                    <p>Tax: <strong>${total * 0.1:.2f}</strong></p>
                    <hr style="border-color: rgba(255,255,255,0.3);">
                    <h4>Total: <strong>${total * 1.1:.2f}</strong></h4>
                    <button class="btn btn-light w-100 mt-3" onclick="checkout()"><i class="fas fa-credit-card"></i> Checkout</button>
                </div>
            </div>
        </div>
        """
    
    html = HTML_CART.format(cart_html=cart_html)
    return html, 200, {"Content-Type": "text/html; charset=utf-8"}

@app.route("/api/add-to-cart", methods=["POST"])
def add_to_cart():
    data = flask.request.get_json()
    cart = flask.session.get('cart', [])
    
    item_id = data.get('id')
    existing = next((item for item in cart if item['id'] == item_id), None)
    
    if existing:
        existing['quantity'] += data.get('quantity', 1)
    else:
        cart.append({
            'id': item_id,
            'name': data.get('name'),
            'price': data.get('price'),
            'quantity': data.get('quantity', 1)
        })
    
    flask.session['cart'] = cart
    cart_count = sum(item['quantity'] for item in cart)
    
    return flask.jsonify({"success": True, "cart_count": cart_count})

@app.route("/api/remove-from-cart", methods=["POST"])
def remove_from_cart():
    data = flask.request.get_json()
    cart = flask.session.get('cart', [])
    cart = [item for item in cart if item['id'] != data.get('id')]
    flask.session['cart'] = cart
    
    return flask.jsonify({"success": True})

@app.route("/api/get-cart-count", methods=["GET"])
def get_cart_count():
    cart = flask.session.get('cart', [])
    count = sum(item['quantity'] for item in cart)
    return flask.jsonify({"count": count})

@app.route("/api/checkout", methods=["POST"])
def checkout():
    flask.session['cart'] = []
    return flask.jsonify({"success": True})

if __name__ == "__main__":
    print("\n" + "="*70)
    print("✅ GENERAL STORE WITH SHOPPING CART IS NOW RUNNING")
    print("="*70)
    print("🌐 OPEN YOUR BROWSER: http://localhost:8080")
    print("="*70 + "\n")
    sys.stdout.flush()
    try:
        app.run(host="0.0.0.0", port=8080, debug=False)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
