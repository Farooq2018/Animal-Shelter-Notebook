from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self,username,password):
        #Initializing the MongoClient. This helps to
        #access the mongodb databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:54575/?authMechanism=DEFAULT&authSource=AAC'%(username, password))
        self.database = self.client['AAC']
        
    #Create method for AAC database
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            #if insert is successful, return true
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
                                                                       
    #Read method for AAC database
    def read(self, criteria = None):
        #If there is no criteria pass to function
        if criteria is None:
            data = self.database.animals.find( {}, {"_id":False})
        #If criteria pass to the function
        else:
            data = self.database.animals.find( criteria, {"_id":False})
        return data
    
    #Update method for AAC database
    def update(self,currentData,newData):
        if currentData is not None:
            updatedData = self.database.animals.update_many(currentData,{"$set":newData})
            return dumps(self.read(newData))
        else:
            raise Exception("Nothing to update, because data parameter is empty")
    
    #Delete method for AAC database
    def delete(self,data):
        if data is not None:
            deletedData = self.database.animals.delete_one(data)
            return dumps(self.read(data))
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            
                                                                     
            