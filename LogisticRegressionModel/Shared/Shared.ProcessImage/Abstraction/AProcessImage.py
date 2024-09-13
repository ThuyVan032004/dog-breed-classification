import cv2
import numpy as np 
import zope.interface
from abc import ABC
import sys 

# sys.path.append('../Shared/Shared.ProcessImage/Model')
sys.path.append('E:/dog_breed_classification/LogisticRegressionModel/Shared/Shared.ProcessImage/Model')
from IProcessImage import IProcessImage

@zope.interface.implementer(IProcessImage)
class AProcessImage(ABC):
    def __init__(self, img_set):
        self.img_set = img_set
        
    def flattenImage(self):
            
        flatten_imgs = []
        for img in self.img_set:
            img = np.array(img).flatten()
            flatten_imgs.append(img)
            
        self.img_set = flatten_imgs
        return self.img_set
    
    def resize(self, sizeX, sizeY):
        size = (sizeX, sizeY)
    
        resized_imgs = []
        
        for img in self.img_set:
            resized_img = np.resize(img, size)
            resized_imgs.append(resized_img)
        
        self.img_set = resized_imgs
        return self.img_set
    
    def attachLabel(self, label):
        X = []
        y = []

        for img in self.img_set:
            X.append(img)
            y.append(label)
        return X, y