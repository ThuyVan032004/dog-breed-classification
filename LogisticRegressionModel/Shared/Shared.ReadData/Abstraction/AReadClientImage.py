from PIL import Image
import pandas as pd 
import zope.interface 
from abc import ABC
import sys 
import os
import base64
from io import BytesIO  
import requests

# sys.path.append('../Shared/Shared.ReadData/Model')
sys.path.append('E:/LogisticRegressionProject/LogisticRegression/Shared/Shared.ReadData/Model')
from IReadData import IReadData

@zope.interface.implementer(IReadData)
class AReadClientImage(ABC):
    def __init__(self, image_url):
        self.image_url = image_url
        
    def readData(self):
        # try:
        image = Image.open(self.image_url).convert('RGB')
        return image
        # except Exception as e:
        #     print(f"Failed to read the image: {str(e)}")
        #     print(f"Image URL: {self.image_url[:100]}...")  # Print first 100 chars of URL
        #     return None  # Return None instead of not returning anything

