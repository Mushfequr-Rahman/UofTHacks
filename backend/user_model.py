'''
# - File: users.py
# - Description: Users class and functions
'''
import datetime

class User():

    def __init__(self, id, privateKey, hashes):
        self.useData = {"_id": id, "privateKey": privateKey, "hashes": hashes, "createdAt": datetime.datetime.now().utcnow()}
    
    def new(self):
        return self.useData   