from Item import *
from bson import Binary, Code
from bson.json_util import dumps, loads
from Item import *
from MongoLibraryUtil import *

def searchItem(collection, query):
    regex = ".*" + query + ".*"
    dbquery = {"Title":{"$regex": regex}}
    result = collection.find(dbquery, {"_id": 0})
    return result

def itemFromDoc(document):
    stock = []
    for i in range(0, len(document["Stock"])-1):
        stock.append(
            Stock(
                document["Stock"][i]["ID"],
                document["Stock"][i]["DueDate"],
                document["Stock"][i]["Type"],
                document["Stock"][i]["RentedTo"],
            )
        )
    return Item(
        document["ISBN"],
        document["Title"],
        document["Author"],
        document["Genre"],
        document["Rating"],
        stock
    )

def insertItemDoc(collection, item):
    stock = []

    for i in range(0, len(item.stock)-1):
        stock.append(
            {
                "ID": item.stock[i].id,
                "DueDate": item.stock[i].due,
                "Type": item.stock[i].type,
                "RentedTo": item.stock[i].rentedTo
            }
        )

    collection.insert_one(
        {
            "ISBN": item.isbn,
            "Title": item.title,
            "Author": item.author,
            "Stock": stock,
            "Genre": item.genre,
            "Rating": item.rating
        }
    )

def updateItemDoc(collection, isbn, field, value):
    collection.update_one(
        {"ISBN": isbn},
        {"$set": {field: value}}
    )

def deleteItemDoc(collection, isbn):
    collection.delete_one(
        {"ISBN": isbn}
    )