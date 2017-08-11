from pymongo import MongoClient
import regex
from bson import Binary, Code
from bson.json_util import dumps, loads
from Item import *
from MongoLibraryUtil import *

conn = MongoClient("localhost:27017")

db = conn.PyLibrary

collection = db.Inventory

results = searchItem(collection, "hitch")

print(itemFromDoc(results[0]).toString())