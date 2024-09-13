from PIL import Image
import pandas as pd 
import zope.interface 
from abc import ABC
import sys 
import os
import glob

sys.path.append('E:/dog_breed_classification/LogisticRegressionModel/Shared/Shared.ReadData/Model')
from IReadData import IReadData 

@ zope.interface.implementer(IReadData)
class AReadLocalImage(ABC):
    def __init__(self, directory, file, format):
        self.__directory = directory 
        self.__file = file 
        self.__format = format 
        
    def readData(self):
        # if image path contain a single image file, return 
        if self.__file != '':
            return Image.open(self.__directory).convert('RGB')
        # if image path is a directory, read images contained in it
        img_collection = [Image.open(img).convert('RGB') for img in glob.glob(os.path.join(self.__directory, f'*.{self.__format}'))]
        return img_collection