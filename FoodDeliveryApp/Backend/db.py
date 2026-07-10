from pymongo import MongoClient

MONGO_URI = "mongodb+srv://krishnadarapaneni85_db_user:KRISHNA%40681d@cluster0.63tdiai.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["FoodDeliveryDB"]

customers_col = db["customers"]
restaurants_col = db["restaurants"]
foods_col = db["foods"]
cart_col = db["cart"]
orders_col = db["orders"]
