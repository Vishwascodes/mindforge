from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Vishwas29_db_user:Vishwas2004@mind-forge-cluster.mcs3fya.mongodb.net/?appName=mind-forge-cluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Select database
db = client["mind-forge"]   # <-- database name

# Select collections
questions_collection = db["questions"]
users_collection = db["users"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
