from pymongo import MongoClient

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
            return True
        except Exception as err:
            print(err)
            return False
    
    def get_tasks(self, collection_name):
        try:
            collection = self.get_collection(collection_name)
            data = list(collection.find({}))
            return data
        except Exception as err:
            print(err)
            return ({'msg': 'Ocurrio un problema'})
            