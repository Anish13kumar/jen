from pymongo import MongoClient

import os

client = MongoClient(str(os.getenv("MONGO_URL")))
db = client[str(os.getenv("MONGODB_NAME"))]


if db != None:
    print("DB Conn Success")
else:
    print("DB Conn Failed")