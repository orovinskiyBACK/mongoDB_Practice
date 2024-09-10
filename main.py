import datetime
from pymongo import MongoClient

cluster = 'mongodb://localhost:27017/practice'
client = MongoClient(cluster)

print(client.list_database_names())

db = client["test"]

print(db.list_collection_names())

todo = {"name": "Patrick", "text": "My first to do!", "status": "open",
        "tags": ["python", "coding"], "date": str(datetime.datetime.now())}

todos = db.todos

#result = todos.insert_one(todo)

todo2 = [{"name": "Patrick", "text": "My Second to do!", "status": "open",
        "tags": ["python", "coding"], "date": str(datetime.datetime.now())},
        {"name": "Mary", "text": "My third to do!", "status": "open",
        "tags": ["c++", "coding"], "date": str(datetime.datetime(2021,1,1,10,45))}]

#results = todos.insert_many(todo2)
from bson.objectid import ObjectId
results = todos.find({"name": "Patrick"}).sort("name")
print(list(results)) # once accessed it is gone

for result in results:
    print(result)

# $ls = less than $gt = greater than (Operators)

#results = todos.delete_many({"name":"Patrick"})
results = todos.update_one({"tags":"python"},{"$set":{"status":"done"}})