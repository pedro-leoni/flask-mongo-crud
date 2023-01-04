from pymongo import MongoClient

client = MongoClient('localhost')
db = client['TasksDB']
resp = list(db['tasks'].find({}))
print(resp)