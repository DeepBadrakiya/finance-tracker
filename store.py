#!/usr/bin/env python3
"""Working General Store - No 403 Errors"""
import flask

app = flask.Flask(__name__)

HTML_HOME = """
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<title>General Store</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
<style>
body { background: linear-gradient(135deg, #667eea, #764ba2); color: white; }
h1, h2 { color: white; }
.btn-light:hover { background: #e0e0e0; }
</style>
</head>
<body>
<nav class="navbar navbar-dark" style="background: rgba(0,0,0,0.3);">
  <div class="container"><span class="navbar-brand fs-4">🛍️ General Store</span></div>
</nav>
<div class="container text-center py-5">
  <h1 class="display-4 mb-4">Welcome to General Store</h1>
  <p class="lead mb-4">Your one-stop shop for quality products</p>
  <a href="/products" class="btn btn-light btn-lg">Shop Now →</a>
</div>
</body>
</html>
"""

HTML_PRODUCTS = """
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<title>Products - General Store</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
<style>
body { background: #f5f5f5; }
.navbar { background: linear-gradient(135deg, #667eea, #764ba2) !important; }
.card { box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: transform 0.3s; }
.card:hover { transform: translateY(-5px); }
.price { color: #667eea; font-size: 1.5rem; font-weight: bold; }
</style>
</head>
<body>
<nav class="navbar navbar-dark">
  <div class="container">
    <a href="/" class="navbar-brand">🛍️ General Store</a>
    <a href="/" class="btn btn-light">← Home</a>
  </div>
</nav>
<div class="container py-5">
  <h2 class="mb-4">Our Products</h2>
  <div class="row">
    <div class="col-md-4 mb-4">
      <div class="card h-100">
        <div class="card-body text-center">
          <h5>💻 Laptop</h5>
          <p class="price">$999.99</p>
          <p class="text-muted">Electronics</p>
          <button class="btn btn-primary">Add to Cart</button>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card h-100">
        <div class="card-body text-center">
          <h5>🖱️ Wireless Mouse</h5>
          <p class="price">$29.99</p>
          <p class="text-muted">Electronics</p>
          <button class="btn btn-primary">Add to Cart</button>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card h-100">
        <div class="card-body text-center">
          <h5>🔌 USB-C Cable</h5>
          <p class="price">$15.99</p>
          <p class="text-muted">Electronics</p>
          <button class="btn btn-primary">Add to Cart</button>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card h-100">
        <div class="card-body text-center">
          <h5>☕ Coffee Maker</h5>
          <p class="price">$89.99</p>
          <p class="text-muted">Appliances</p>
          <button class="btn btn-primary">Add to Cart</button>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card h-100">
        <div class="card-body text-center">
          <h5>🥤 Blender</h5>
          <p class="price">$49.99</p>
          <p class="text-muted">Appliances</p>
          <button class="btn btn-primary">Add to Cart</button>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card h-100">
        <div class="card-body text-center">
          <h5>🍞 Toaster</h5>
          <p class="price">$34.99</p>
          <p class="text-muted">Appliances</p>
          <button class="btn btn-primary">Add to Cart</button>
        </div>
      </div>
    </div>
  </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    return HTML_HOME, 200, {"Content-Type": "text/html; charset=utf-8"}

@app.route("/products", methods=["GET", "POST"])  
def products():
    return HTML_PRODUCTS, 200, {"Content-Type": "text/html; charset=utf-8"}

if __name__ == "__main__":
    print("\n" + "="*70)
    print("✅ GENERAL STORE IS RUNNING")
    print("="*70)
    print("🌐 Open your browser: http://localhost:5000")
    print("="*70 + "\n")
    app.run(host="localhost", port=5000, debug=False, use_reloader=False)
