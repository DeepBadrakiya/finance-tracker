#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>General Store</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
            .container { margin-top: 100px; text-align: center; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🛍️ General Store</h1>
            <p class="lead">Welcome to our store!</p>
            <a href="/products" class="btn btn-light btn-lg">Shop Now</a>
        </div>
    </body>
    </html>
    '''

@app.route('/products')
def products():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Products</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <nav class="navbar navbar-dark bg-primary">
            <div class="container">
                <span class="navbar-brand">General Store</span>
                <a href="/" class="btn btn-light">Home</a>
            </div>
        </nav>
        <div class="container py-5">
            <h2>Products</h2>
            <div class="row">
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-body">
                            <h5>Laptop</h5>
                            <p class="text-danger">$999.99</p>
                            <button class="btn btn-primary">Add to Cart</button>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-body">
                            <h5>Mouse</h5>
                            <p class="text-danger">$29.99</p>
                            <button class="btn btn-primary">Add to Cart</button>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-body">
                            <h5>Cable</h5>
                            <p class="text-danger">$15.99</p>
                            <button class="btn btn-primary">Add to Cart</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("\n" + "="*60)
    print("✅ GENERAL STORE APP - RUNNING NOW")
    print("="*60)
    print("🌐 URL: http://localhost:5000")
    print("🏠 HOME: http://localhost:5000/")
    print("🛍️  SHOP: http://localhost:5000/products")
    print("⚠️  STOP: Press Ctrl+C")
    print("="*60 + "\n")
    app.run(host='localhost', port=5000, debug=False)
