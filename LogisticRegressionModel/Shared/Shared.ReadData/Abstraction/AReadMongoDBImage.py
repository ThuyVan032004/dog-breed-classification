from PIL import Image
import cv2
import zope.interface 
from abc import ABC
import sys 
import os
import glob
from pymongo import MongoClient

sys.path.append('E:/dog_breed_classification/LogisticRegressionModel/Shared/Shared.ReadData/Model')
from IReadData import IReadData

@ zope.interface.implementer(IReadData)
class AReadMongoDBImage(ABC):
    def __init__(self, uri, database_name):
        self.uri = uri 
        self.database_name = database_name 
        self.client = MongoClient(self.uri)

    def readData(self):
        self.db = self.client[self.database_name]
        collection_list = self.db.list_collection_names()
        
        all_documents = []
        for collection in collection_list:
            documents = self.db[collection].find({})
            all_documents.extend(documents)
        
        X = []
        y = []
        for document in all_documents:
            rgb_img = Image.open(document['imageUrl']).convert('RGB')
            label = document['label']
            X.append(rgb_img)
            y.append(label)
        
        return X, y
        
            
        
            
        
    
    



    