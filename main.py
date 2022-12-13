# Backend for passMan project
from pymongo import MongoClient

class DataBase:
    def __init__(self, db_name, collection_name) -> None:
        self.client = MongoClient("mongodb+srv://khudoberdi:GbyJeM7ltbC4KpYP@cluster0.5afpfbk.mongodb.net/?retryWrites=true&w=majority")

        self.current_db = self.client[db_name]
        self.collection = self.current_db[collection_name]
    
    def add(self, data: dict, many = False):
        if many:
            ins_result = self.collection.insert_many(data)
            return ins_result.inserted_ids
        else:
            ins_result = self.collection.insert_one(data)
            return ins_result.inserted_id
    
    def find(self, data: dict, delete = False, count = False, update = False, updatedData = []):
        if delete:
            return self.collection.find_one_and_delete(data)
        if count:
            return self.collection.count_documents(data)
        if update:
            if not updatedData:
                return self.collection.find_one_and_update(data, updatedData)
            return {"message": 'New data is not found'}
        return self.collection.find_one(data)
    
    def findAll(self):
        return [i for i in self.collection.find()]
