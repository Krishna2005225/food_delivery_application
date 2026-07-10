# Food Delivery Application

A full-stack food delivery web application built with Django for backend services and a responsive HTML/CSS/JavaScript frontend.

## Project Overview

This project simulates a food delivery platform where customers can browse restaurants, view menus, add items to a cart, and place orders. It also includes a simple admin dashboard for managing customers, restaurants, food items, and orders.

## Key Features

- Browse restaurants with search and filters
- View restaurant-specific menu items
- Add food items to cart with quantity controls
- Checkout and place orders
- View current orders and order history
- Admin dashboard to manage customers, restaurants, foods, and orders
- Local image support for restaurants and food items

## Project Structure

- `FoodDeliveryApp/`
  - `manage.py` - Django management entrypoint
  - `seed_data.py` - Seed script for MongoDB sample data
  - `Backend/`
    - `__init__.py`
    - `db.py` - MongoDB connection and collections
    - `settings.py` - Django settings
    - `urls.py` - URL routing for frontend pages and API endpoints
    - `views.py` - API view implementations
    - `wsgi.py` - WSGI application entrypoint
  - `Frontend/`
    - `index.html`, `login.html`, `register.html`, `restaurants.html`, `menu.html`, `cart.html`, `orders.html`, `dashboard.html`
    - `script.js` - frontend logic for UI interactions and API calls
    - `style.css` - application styling
    - `images/` - local image assets for restaurants and foods

## Technologies Used

- Python
- Django
- MongoDB
- HTML, CSS, JavaScript

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/Krishna2005225/food_delivery_application.git
   cd food_delivery_application/FoodDeliveryApp
   ```

2. Install dependencies (if any) and configure Python environment.

3. Seed the database with sample data:

   ```bash
   python seed_data.py
   ```

4. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

5. Open the app in your browser at:

   ```
   http://127.0.0.1:8000/
   ```

## Notes

- This project uses MongoDB for data storage.
- The app serves frontend static assets and pages directly via Django routes.
- The admin dashboard is not a secured admin panel; it is a simple management UI.

## Recommended Improvements

- Add a proper login/register backend flow with authentication.
- Secure admin dashboard access.
- Improve data validation and error handling.
- Add persistent static file handling using Django `staticfiles`.
- Replace placeholder SVG images with real restaurant and food photos.

## Repository

https://github.com/Krishna2005225/food_delivery_application
