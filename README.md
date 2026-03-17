# General Store Web Application

A beautiful, full-featured e-commerce web application built with Flask and Bootstrap. Perfect for learning web development or as a starter template for an online store.

## Features

✨ **Product Management**
- Browse products by category
- View detailed product information
- Product search and filtering
- Stock availability tracking

🛒 **Shopping Cart**
- Add/remove items from cart
- Real-time cart count updates
- Persistent cart session management
- Easy checkout process

📦 **Order Management**
- Complete order history
- Order tracking and status
- Customer information capture
- Order confirmation

🎨 **Beautiful UI**
- Modern responsive design with Bootstrap 5
- Gradient color scheme with animations
- Mobile-friendly interface
- Smooth transitions and hover effects
- Font Awesome icons

🔒 **Features**
- Session-based cart management
- JSON file storage for orders
- Error handling and validation
- Flash notifications

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/DeepBadrakiya/finance-tracker.git
cd finance-tracker
```

2. **Create virtual environment** (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python general_store_app.py
```

5. **Open in browser**
Navigate to `http://localhost:5000`

## Project Structure

```
general-store/
├── general_store_app.py      # Main Flask application
├── requirements.txt          # Python dependencies
├── store_data.json          # Orders storage (auto-created)
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── index.html          # Home page
│   ├── products.html       # Product listing
│   ├── product_detail.html # Product details
│   ├── cart.html           # Shopping cart
│   ├── orders.html         # Order history
│   ├── about.html          # About page
│   └── 404.html            # Error page
└── static/                 # Static files
    ├── css/
    │   └── style.css       # Custom styling
    └── js/
        └── main.js         # JavaScript functionality
```

## Usage

### Home Page
- Welcome section with store information
- Category shortcuts
- Statistics dashboard

### Products Page
- View all products or filter by category
- Add items to cart
- Quick view product details

### Shopping Cart
- Review cart items
- Remove items
- View order summary
- Proceed to checkout

### Checkout
- Enter delivery information
- Place order
- Order confirmation

### Orders Page
- View all placed orders
- Order details and status
- Delivery information

## Sample Products

The application comes pre-loaded with sample products:
- **Electronics**: Laptop, Wireless Mouse, USB-C Cable
- **Appliances**: Coffee Maker, Blender, Toaster
- **Office**: Desk Lamp, Office Chair
- **Furniture**: Bookshelf
- **Decor**: Wall Clock

## Customization

### Add New Products
Edit `PRODUCTS` list in `general_store_app.py`:
```python
PRODUCTS = [
    {
        "id": 11,
        "name": "Your Product",
        "price": 99.99,
        "category": "Your Category",
        "image": "product.jpg",
        "stock": 50
    },
    ...
]
```

### Modify Styling
Edit `static/css/style.css` to change colors, fonts, and layouts.

### Change Store Info
Update footer and header content in `templates/base.html`.

## Database

The application uses JSON files for data storage:
- **store_data.json**: Stores all customer orders

## API Endpoints

### Add to Cart
```
POST /api/add-to-cart
{
    "product_id": 1,
    "quantity": 1
}
```

### Remove from Cart
```
POST /api/remove-from-cart/<product_id>
```

### Checkout
```
POST /api/checkout
{
    "name": "Customer Name",
    "email": "email@example.com",
    "address": "Delivery Address"
}
```

## Technologies Used

- **Backend**: Flask 2.3.0
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Storage**: JSON files
- **Icons**: Font Awesome 6.0

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Performance Features

- Lazy loading
- Optimized CSS and JavaScript
- Responsive images
- Smooth animations
- Fast checkout process

## Security Notes

⚠️ **Important**: This is a demonstration application. For production use:
- Use a proper database (PostgreSQL, MongoDB, etc.)
- Implement user authentication
- Use HTTPS/SSL
- Implement payment gateway integration
- Add CSRF protection
- Sanitize all user inputs
- Use environment variables for sensitive data

## Deployment

### Deploy to Heroku
```bash
heroku create your-store-name
git push heroku main
```

### Deploy to AWS/Azure
Follow their respective documentation for Flask applications.

## Future Enhancements

- [ ] User accounts and authentication
- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] Email notifications
- [ ] Admin dashboard
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Search bar with autocomplete
- [ ] Multiple payment methods
- [ ] Inventory management
- [ ] Analytics and reports

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Author

Created with ❤️ by [Deep Badrakiya](https://github.com/DeepBadrakiya)

---

**Happy Coding! 🚀**
