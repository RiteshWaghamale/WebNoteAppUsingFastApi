# from pymongo import MongoClient

# MONGO_URI ="mongodb+srv://riteshwaghamale9112:2CZFAvkbcQHhfQuR@cluster0.iepry2b.mongodb.net"

# conn = MongoClient(MONGO_URI)

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()   # ✅ LOAD ENV HERE

MONGO_URI = os.getenv("MONGO_URL")

if not MONGO_URI:
    raise Exception("MONGO_URL not found in environment variables")

conn = MongoClient(MONGO_URI)
