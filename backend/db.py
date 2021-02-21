'''
Filename: db.py
- Database Connection
'''

# MongoDB library
import pymongo
import urllib.parse
from pymongo import MongoClient

# Database class
class database():
    def __init__(self):
        dbuser = urllib.parse.quote_plus("UofTIPFSDB")
        dbpass = urllib.parse.quote_plus("2U&@_zjDB")
        
        self.config = {"mongodb": "mongodb://"+dbuser+":"+dbpass+"@143.110.222.148:27017/?authSource=admin", 
                       "cluster": "P2BoxDB",
                       "collection": "Users"}
        self.dbFailed = "[ MongoDB ] Operation Failed"
        self.db = self.connect()
        

    def connect(self):
        '''
        Connecting to the database.
        param: self
        return: database of the cluster
        '''

        cluster = MongoClient(self.config["mongodb"])
        db = cluster[self.config["cluster"]]
        return db
    
    def insert(self, user, collection="Users"):
        '''
        Inserting a new data to the database.
        The function will change depending if the data
        is a list or just one.
        '''
        if type(user) == list:
            try:
                self.db[collection].insert_many(user)
                return True
            except pymongo.errors.OperationFailure:
                print(self.dbFailed)
                return False
        else:
            try: 
                self.db[collection].insert_one(user)
                return True
            except pymongo.errors.OperationFailure:
                print(self.dbFailed)
                return False


    def delete(self, id, collection="Users"):
        '''
        Deleting a data from database
        '''
        try: 
            self.db[collection].delete_one({"_id": id})
            return True
        except pymongo.errors.OperationFailure:
            print(self.dbFailed)
            return False


    def find(self, id, collection="Users"):
        '''
        Getting the details of a specific record - id
        '''
        try: 
            return self.db[collection].find_one({"_id": id})
        except pymongo.errors.OperationFailure:
            print(self.dbFailed)
            return False


    def find_reminder(self, reminderValue=True, collection="Users"):
        '''
        Finding all the users who have set the reminder to TRUE
        '''
        try:
            return self.db[collection].find({"reminder": {"status": reminderValue}})
        except pymongo.errors.OperationFailure:
            print(self.dbFailed)
            return False

    def update(self, id, fieldName, newValue, subField=None, collection="Users"):

    
        '''
        Updates the "fieldName" with the id of "id"
        and value of "newValue"
        INFO: if you want to update a field inside another field
        ex: settings->campus, you have to specify the name of the parent field.
        So if we want to update campus, in the subField we have to write "settings"
        '''
        if subField == None:
            try:
                self.db[collection].update_one({"_id": id}, 
                                           {"$set": {fieldName: newValue}})
                return True
            except pymongo.errors.OperationFailure:
                print(self.dbFailed)
                return False
        else:
            try:
                self.db[collection].update_one({"_id": id}, 
                                           {"$set": {subField: {fieldName: newValue}}})
                return True
            except pymongo.errors.OperationFailure:
                print(self.dbFailed)
                return False

