from pymongo import MongoClient
from datetime import datetime

stockDB = 'mydb'
dbname = "howard-good31"


def constructor_stock():
    client = MongoClient(
        "mongodb://av2288444:t0955787053S@ac-gbnruue-shard-00-00.kt0hhit.mongodb.net:27017,ac-gbnruue-shard-00-01.kt0hhit.mongodb.net:27017,ac-gbnruue-shard-00-02.kt0hhit.mongodb.net:27017/?ssl=true&replicaSet=atlas-r0k35s-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client[stockDB]
    return db


def update_my_stock(user_name, stockNumber, condition, target_price):
    db = constructor_stock()
    collect = db[user_name]
    collect.update_many({"favorite_stock": stockNumber}, {'$set': {'condition': condition, "price": target_price}})
    content = f"股票{stockNumber}更新成功"
    return content


def write_my_stock(userID, user_name, stockNumber, condition, target_price):
    db = constructor_stock()
    collect = db[user_name]
    is_exit = collect.find_one({'favorite_stock': stockNumber})
    if is_exit != None:
        content = update_my_stock(user_name, stockNumber, condition, target_price)
        return content
    else:
        collect.insert_one({
            "userID": userID,
            "favorite_stock": stockNumber,
            "condition": condition,
            "price": target_price,
            "tag": "stock",
            "date_info": datetime.now()
        })
        return f"{stockNumber} 已新增您的股票清單"
