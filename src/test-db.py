from pymongo import MongoClient

client = MongoClient('localhost')
db = client['TasksDB']
id = "63b75471620889a6cd2ec95a"
result = db['tasks'].delete_one({"name": "tarea2"})
print(result.deleted_count)