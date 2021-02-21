'''
# - File: users.py
# - Description: Users class and functions
'''
import datetime

# MARK: User Class
class User():

    def __init__(self, id, privateKey, hashes, user, password):
        self.useData = {"user": user, "pwd": password, "privateKey": privateKey, "hashes": hashes, "createdAt": datetime.datetime.now().utcnow()}
    
    def new(self):
        return self.useData   


# MARK: - Hash Class
class Hashes():

    def __init__(self, hasdID, timeCreated):
        self.hashData = {"hash": hasdID, "time": timeCreated}
    
    def new(self):
        return self.hashData