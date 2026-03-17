// General Store Main JavaScript

// Update cart count in navbar
function updateCartCount(count) {
    const cartCount = document.getElementById('cart-count');
    if (cartCount) {
        if (count > 0) {
            cartCount.textContent = count;
            cartCount.style.display = 'inline-block';
        } else {
            cartCount.style.display = 'none';
        }
    }
}

// Show notification
function showNotification(message, type = 'success') {
    const alertClass = type === 'success' ? 'alert-success' : 'alert-danger';
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert ${alertClass} position-fixed top-0 end-0 m-3`;
    alertDiv.setAttribute('role', 'alert');
    alertDiv.textContent = message;
    alertDiv.style.zIndex = '9999';
    alertDiv.style.minWidth = '300px';
    
    document.body.appendChild(alertDiv);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        alertDiv.remove();
    }, 3000);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Add to cart button listeners
    document.querySelectorAll('.add-to-cart-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const productId = this.dataset.productId;
            const productName = this.dataset.productName;
            const price = this.dataset.productPrice;
            addToCart(productId, productName, price);
        });
    });

    // Add product to cart button listeners
    document.querySelectorAll('.add-product-to-cart-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const productId = this.dataset.productId;
            const productName = this.dataset.productName;
            const price = this.dataset.productPrice;
            addProductToCart(productId, productName, price);
        });
    });

    // Remove item button listeners
    document.querySelectorAll('.remove-item-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const productId = this.dataset.productId;
            removeFromCart(productId);
        });
    });

    // Checkout form handler
    const checkoutForm = document.getElementById('checkoutForm');
    if (checkoutForm) {
        checkoutForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const orderData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                address: document.getElementById('address').value
            };
            
            fetch('/api/checkout', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(orderData)
            })
            .then(r => r.json())
            .then(data => {
                if (data.success) {
                    showNotification('✓ Order placed! Order ID: ' + data.order_id, 'success');
                    setTimeout(() => window.location.href = '/orders', 1000);
                } else {
                    showNotification('❌ ' + data.message, 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showNotification('Error placing order', 'error');
            });
        });
    }

    console.log('General Store loaded successfully');
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Form validation
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Product search functionality
function searchProducts(query) {
    const cards = document.querySelectorAll('.product-card');
    query = query.toLowerCase();
    
    cards.forEach(card => {
        const productName = card.querySelector('.card-title').textContent.toLowerCase();
        if (productName.includes(query)) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
}

// Cart management
function addToCart(productId, productName, price) {
    fetch('/api/add-to-cart', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            product_id: productId,
            quantity: 1
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification('✓ ' + productName + ' added to cart!', 'success');
            updateCartCount(data.cart_count);
        } else {
            showNotification('❌ ' + data.message, 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Error adding to cart', 'error');
    });
}

// Add product to cart with quantity
function addProductToCart(productId, productName, price) {
    const quantity = parseInt(document.getElementById('quantity').value) || 1;
    
    fetch('/api/add-to-cart', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            product_id: productId,
            quantity: quantity
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification('✓ ' + quantity + 'x ' + productName + ' added to cart!', 'success');
            updateCartCount(data.cart_count);
        } else {
            showNotification('❌ ' + data.message, 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Error adding to cart', 'error');
    });
}

// Remove from cart
function removeFromCart(productId) {
    if (confirm('Are you sure you want to remove this item?')) {
        fetch('/api/remove-from-cart/' + productId, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showNotification('Item removed from cart', 'success');
                updateCartCount(data.cart_count);
                // Remove from DOM
                const row = document.querySelector('[data-product-id="' + productId + '"]');
                if (row) row.remove();
                
                // Reload if cart is now empty
                if (data.cart_count === 0) {
                    setTimeout(() => location.reload(), 500);
                }
            } else {
                showNotification('Error removing item', 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showNotification('Error removing item', 'error');
        });
    }
}

// Format price
function formatPrice(price) {
    return '$' + parseFloat(price).toFixed(2);
}

// Convert timestamp to readable date
function formatDate(timestamp) {
    const date = new Date(timestamp * 1000);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}
