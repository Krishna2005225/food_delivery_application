import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Backend.db import customers_col, restaurants_col, foods_col, cart_col, orders_col

customers_col.drop()
restaurants_col.drop()
foods_col.drop()
cart_col.drop()
orders_col.drop()

customers_col.insert_one({
    "customer_id": 101,
    "full_name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "phone": "9876543210",
    "address": "KPHB Colony",
    "city": "Hyderabad"
})

restaurants = [
    {
        "restaurant_id": 201,
        "restaurant_name": "Spicy Kitchen",
        "owner_name": "Kiran Kumar",
        "location": "Hyderabad",
        "cuisine": "South Indian",
        "rating": 4.6,
        "image": "/images/restaurant-1.svg"
    },
    {
        "restaurant_id": 202,
        "restaurant_name": "Pizza Palace",
        "owner_name": "Amit Reddy",
        "location": "Bangalore",
        "cuisine": "Italian",
        "rating": 4.3,
        "image": "/images/restaurant-2.svg"
    },
    {
        "restaurant_id": 203,
        "restaurant_name": "Dragon Wok",
        "owner_name": "Mei Chen",
        "location": "Mumbai",
        "cuisine": "Chinese",
        "rating": 4.4,
        "image": "/images/restaurant-3.svg"
    },
    {
        "restaurant_id": 204,
        "restaurant_name": "Curry House",
        "owner_name": "Priya Patel",
        "location": "Delhi",
        "cuisine": "North Indian",
        "rating": 4.5,
        "image": "/images/restaurant-4.svg"
    }
]
restaurants_col.insert_many(restaurants)

foods = [
    {
        "food_id": 301,
        "restaurant_name": "Spicy Kitchen",
        "food_name": "Chicken Biryani",
        "category": "Main Course",
        "price": 299,
        "availability": "Available",
        "image": "/images/food-1.svg"
    },
    {
        "food_id": 302,
        "restaurant_name": "Spicy Kitchen",
        "food_name": "Paneer Butter Masala",
        "category": "Main Course",
        "price": 249,
        "availability": "Available",
        "image": "/images/food-2.svg"
    },
    {
        "food_id": 303,
        "restaurant_name": "Spicy Kitchen",
        "food_name": "Masala Dosa",
        "category": "Starters",
        "price": 120,
        "availability": "Available",
        "image": "/images/food-3.svg"
    },
    {
        "food_id": 304,
        "restaurant_name": "Spicy Kitchen",
        "food_name": "Gulab Jamun",
        "category": "Desserts",
        "price": 80,
        "availability": "Available",
        "image": "/images/food-4.svg"
    },
    {
        "food_id": 305,
        "restaurant_name": "Spicy Kitchen",
        "food_name": "Idli Sambar",
        "category": "Starters",
        "price": 90,
        "availability": "Out of Stock",
        "image": "/images/food-1.svg"
    },
    {
        "food_id": 306,
        "restaurant_name": "Pizza Palace",
        "food_name": "Margherita Pizza",
        "category": "Main Course",
        "price": 350,
        "availability": "Available",
        "image": "/images/food-2.svg"
    },
    {
        "food_id": 307,
        "restaurant_name": "Pizza Palace",
        "food_name": "Pasta Alfredo",
        "category": "Main Course",
        "price": 280,
        "availability": "Available",
        "image": "/images/food-3.svg"
    },
    {
        "food_id": 308,
        "restaurant_name": "Pizza Palace",
        "food_name": "Garlic Bread",
        "category": "Starters",
        "price": 150,
        "availability": "Available",
        "image": "/images/food-4.svg"
    },
    {
        "food_id": 309,
        "restaurant_name": "Dragon Wok",
        "food_name": "Hakka Noodles",
        "category": "Main Course",
        "price": 180,
        "availability": "Available",
        "image": "/images/food-1.svg"
    },
    {
        "food_id": 310,
        "restaurant_name": "Dragon Wok",
        "food_name": "Manchurian",
        "category": "Starters",
        "price": 160,
        "availability": "Available",
        "image": "/images/food-2.svg"
    },
    {
        "food_id": 311,
        "restaurant_name": "Curry House",
        "food_name": "Butter Chicken",
        "category": "Main Course",
        "price": 320,
        "availability": "Available",
        "image": "/images/food-3.svg"
    },
    {
        "food_id": 312,
        "restaurant_name": "Curry House",
        "food_name": "Naan Bread",
        "category": "Starters",
        "price": 60,
        "availability": "Available",
        "image": "/images/food-4.svg"
    }
]
foods_col.insert_many(foods)

print("Sample data with images seeded successfully!")
print(f"  Customers: {customers_col.count_documents({})}")
print(f"  Restaurants: {restaurants_col.count_documents({})}")
print(f"  Foods: {foods_col.count_documents({})}")
