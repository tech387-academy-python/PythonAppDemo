from pymongo import MongoClient
import logging as log
import webscraper, json, random

class MongoAPI:
       
    def __init__(self, data):
        #self.client = MongoClient('mongodb://mymongo_1:27017/')
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = data['database']
        self.collection = data['collection']
        self.cursor = self.client[self.database]
        self.collection = self.cursor[self.collection] 
        self.data = data   
    
    
    def read(self):
        
        log.info('Writing data')
        documents = self.collection.find()
        
        output = []

        for data in documents:
            temp = {}
            for item in data:
                if item != '_id':
                    temp[item] = data[item]
            output.append(temp)
            
        return output
    
    def write(self):
    
        log.info('Writing data')
        new_document = self.data['document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                'Document_ID' : str(response.inserted_id)}
        
        return output
    
    def delete(self):
        
        log.info('Writing data')
        fltr = self.data['document']
        response = self.collection.delete_one(fltr)
        output = {'Status': 'Successfully deleted' if response.deleted_count > 0 else 'Document not found'}
        
        return output
    
    def populate(self):
        
        log.info('Writing data')
        webscraper.scrapCars()
        
        with open ('data.json', 'r') as f:
            json_data = json.load(f)
            
            car_list = []
            
            for item in json_data:
                car_list.append(item)    
        
        self.collection.update_many({}, {'$set': {'car': random.choice(car_list)}})
            

if __name__ == '__main__':
    print()