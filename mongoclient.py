from pymongo import MongoClient


client = MongoClient("mongodb+srv://ironket_db_user:<db_password>@goitlearn.vejdayj.mongodb.net/")


db = client["authors"]
collection = db["authors"]


db = client["quotes"]
collection = db["quotes"]

