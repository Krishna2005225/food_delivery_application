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
        "image": "https://images.pexels.com/photos/8818667/pexels-photo-8818667.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "restaurant_id": 202,
        "restaurant_name": "Pizza Palace",
        "owner_name": "Amit Reddy",
        "location": "Bangalore",
        "cuisine": "Italian",
        "rating": 4.3,
        "image": "https://images.pexels.com/photos/315755/pexels-photo-315755.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "restaurant_id": 203,
        "restaurant_name": "Dragon Wok",
        "owner_name": "Mei Chen",
        "location": "Mumbai",
        "cuisine": "Chinese",
        "rating": 4.4,
        "image": "https://images.pexels.com/photos/1907228/pexels-photo-1907228.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "restaurant_id": 204,
        "restaurant_name": "Curry House",
        "owner_name": "Priya Patel",
        "location": "Delhi",
        "cuisine": "North Indian",
        "rating": 4.5,
        "image": "https://images.pexels.com/photos/958545/pexels-photo-958545.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
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
        "image": "https://images.pexels.com/photos/28909537/pexels-photo-28909537.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "food_id": 302,
        "restaurant_name": "Spicy Kitchen",
        "food_name": "Paneer Butter Masala",
        "category": "Main Course",
        "price": 249,
        "availability": "Available",
        "image": "https://images.pexels.com/photos/2569760/pexels-photo-2569760.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "food_id": 303,
        "restaurant_name": "Spicy Kitchen",
        "food_name": "Masala Dosa",
        "category": "Starters",
        "price": 120,
        "availability": "Available",
        "image": "https://images.pexels.com/photos/941869/pexels-photo-941869.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "food_id": 304,
        "restaurant_name": "Spicy Kitchen",
        "food_name": "Gulab Jamun",
        "category": "Desserts",
        "price": 80,
        "availability": "Available",
        "image": "https://images.pexels.com/photos/11887844/pexels-photo-11887844.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "food_id": 305,
        "restaurant_name": "Spicy Kitchen",
        "food_name": "Idli Sambar",
        "category": "Starters",
        "price": 90,
        "availability": "Out of Stock",
        "image": "https://images.pexels.com/photos/8312083/pexels-photo-8312083.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "food_id": 306,
        "restaurant_name": "Pizza Palace",
        "food_name": "Margherita Pizza",
        "category": "Main Course",
        "price": 350,
        "availability": "Available",
        "image": "https://images.pexels.com/photos/315755/pexels-photo-315755.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "food_id": 307,
        "restaurant_name": "Pizza Palace",
        "food_name": "Pasta Alfredo",
        "category": "Main Course",
        "price": 280,
        "availability": "Available",
        "image": "https://images.pexels.com/photos/4518844/pexels-photo-4518844.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "food_id": 308,
        "restaurant_name": "Pizza Palace",
        "food_name": "Garlic Bread",
        "category": "Starters",
        "price": 150,
        "availability": "Available",
        "image": "https://images.pexels.com/photos/1775043/pexels-photo-1775043.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "food_id": 309,
        "restaurant_name": "Dragon Wok",
        "food_name": "Hakka Noodles",
        "category": "Main Course",
        "price": 180,
        "availability": "Available",
        "image": "https://images.pexels.com/photos/1907228/pexels-photo-1907228.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "food_id": 310,
        "restaurant_name": "Dragon Wok",
        "food_name": "Manchurian",
        "category": "Starters",
        "price": 160,
        "availability": "Available",
        "image": "https://images.pexels.com/photos/6996084/pexels-photo-6996084.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "food_id": 311,
        "restaurant_name": "Curry House",
        "food_name": "Butter Chicken",
        "category": "Main Course",
        "price": 320,
        "availability": "Available",
        "image": "https://images.pexels.com/photos/2347311/pexels-photo-2347311.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    },
    {
        "food_id": 312,
        "restaurant_name": "Curry House",
        "food_name": "Naan Bread",
        "category": "Starters",
        "price": 60,
        "availability": "Available",
        "image": "https://images.pexels.com/photos/1893556/pexels-photo-1893556.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&dpr=1"
    }
]
foods_col.insert_many(foods)

print("Sample data with images seeded successfully!")
print(f"  Customers: {customers_col.count_documents({})}")
print(f"  Restaurants: {restaurants_col.count_documents({})}")
print(f"  Foods: {foods_col.count_documents({})}")
