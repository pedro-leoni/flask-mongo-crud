from pymongo import MongoClient
from bson import ObjectId
# TODO make tasks schema

class TasksDB:
    def __init__(self):
        # conect local database client
        self.client = MongoClient('localhost')
        # select db in client
        self.db = self.client['TasksDB']
        print('Local database ready')

    def get_collection(self, collection_name):
        '''
        to select collection make sure you have inserted
        information into the collection manually once 
        because if it is empty it will not take it as existing
        :return: collection to manipulate
        TODO fix mentioned improve
        '''
        collections = self.db.list_collection_names()
        if collection_name not in collections:
            print('collection {} not found in database'.format(collection_name))
            return None
        c = self.db[collection_name]
        return c

    def insert_task(self, collection_name, payload):
        '''
        :return: boolean with process result
        TODO control
        '''
        try:
            collection = self.get_collection(collection_name)
            collection.insert_one(payload)
        except Exception as err:
            raise ValueError(err)
    
    def get_tasks(self, collection_name):
        try:
            collection = self.get_collection(collection_name)
            data = list(collection.find({}))
            return data
        except Exception as err:
            raise ValueError(err)

    def delete_task(self, collection_name, id):
        try:
            object_id = ObjectId(id)
            collection = self.get_collection(collection_name)
            resp = collection.delete_one({'_id': object_id})
            if resp.deleted_count == 0:
                raise ValueError('Not found')
        except Exception as err:
            raise ValueError(err)

    def edit_task(self, collection_name, id, payload):
        try:
            object_id = ObjectId(id)
            collection = self.get_collection(collection_name)
            resp = collection.find_one_and_update({'_id': object_id}, {'$set': payload})
            print(resp)
        except Exception as err:
            raise ValueError(err)

