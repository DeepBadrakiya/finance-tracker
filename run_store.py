#!/usr/bin/env python3
"""General Store - Working Version on Port 8080"""
import flask
import sys

app = flask.Flask(__name__)

HTML_HOME = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>General Store</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
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
<style>
body { background: #f5f5f5; }
.navbar { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important; }
.card { box-shadow: 0 4px 15px rgba(0,0,0,0.2); border: none; transition: transform 0.3s, box-shadow 0.3s; }
.card:hover { transform: translateY(-10px); box-shadow: 0 8px 25px rgba(0,0,0,0.3); }
.price { color: #667eea; font-size: 1.8rem; font-weight: bold; }
.btn-primary { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border: none; }
.btn-primary:hover { background: linear-gradient(135deg, #764ba2 0%, #667eea 100%); }
</style>
</head>
<body>
<nav class="navbar navbar-dark">
<div class="container">
<span class="navbar-brand fs-4 fw-bold">🛍️ General Store</span>
<a href="/" class="btn btn-light btn-sm">← Back Home</a>
</div>
</nav>
<div class="container py-5">
<h2 class="mb-5">Our Featured Products</h2>
<div class="row">
<div class="col-md-4 mb-4">
<div class="card h-100">
<div class="card-body text-center">
<h5 class="card-title">💻 Laptop</h5>
<p class="price">$999.99</p>
<p class="text-muted mb-3">High Performance Electronics</p>
<button class="btn btn-primary w-100">Add to Cart</button>
</div>
</div>
</div>
<div class="col-md-4 mb-4">
<div class="card h-100">
<div class="card-body text-center">
<h5 class="card-title">🖱️ Wireless Mouse</h5>
<p class="price">$29.99</p>
<p class="text-muted mb-3">Precision Electronics</p>
<button class="btn btn-primary w-100">Add to Cart</button>
</div>
</div>
</div>
<div class="col-md-4 mb-4">
<div class="card h-100">
<div class="card-body text-center">
<h5 class="card-title">🔌 USB-C Cable</h5>
<p class="price">$15.99</p>
<p class="text-muted mb-3">Fast Charging Electronics</p>
<button class="btn btn-primary w-100">Add to Cart</button>
</div>
</div>
</div>
<div class="col-md-4 mb-4">
<div class="card h-100">
<div class="card-body text-center">
<h5 class="card-title">☕ Coffee Maker</h5>
<p class="price">$89.99</p>
<p class="text-muted mb-3">Premium Appliances</p>
<button class="btn btn-primary w-100">Add to Cart</button>
</div>
</div>
</div>
<div class="col-md-4 mb-4">
<div class="card h-100">
<div class="card-body text-center">
<h5 class="card-title">🥤 Blender</h5>
<p class="price">$49.99</p>
<p class="text-muted mb-3">Powerful Appliances</p>
<button class="btn btn-primary w-100">Add to Cart</button>
</div>
</div>
</div>
<div class="col-md-4 mb-4">
<div class="card h-100">
<div class="card-body text-center">
<h5 class="card-title">🍞 Toaster</h5>
<p class="price">$34.99</p>
<p class="text-muted mb-3">Modern Appliances</p>
<button class="btn btn-primary w-100">Add to Cart</button>
</div>
</div>
</div>
</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""

@app.route("/", methods=["GET", "POST"])
def home():
    return HTML_HOME, 200, {"Content-Type": "text/html; charset=utf-8"}

@app.route("/products", methods=["GET", "POST"])  
def products():
    return HTML_PRODUCTS, 200, {"Content-Type": "text/html; charset=utf-8"}

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    print("\n" + "="*70)
    print("✅ GENERAL STORE IS NOW RUNNING")
    print("="*70)
    print("🌐 OPEN YOUR BROWSER: http://localhost:8080")
    print("="*70 + "\n")
    sys.stdout.flush()
    try:
        app.run(host="0.0.0.0", port=8080, debug=False)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
