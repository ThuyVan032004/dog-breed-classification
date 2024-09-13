import sys 

# paths = ['../Shared/Shared.ReadData/Abstraction']
sys.path.append('E:/dog_breed_classification/LogisticRegressionModel/Shared/Shared.ReadData/Abstraction')
    
from AReadClientImage import AReadClientImage 
from abc import ABC

class ReadClientImage(AReadClientImage):
    def __init__(self, image_url):
        super().__init__(image_url)