import sys 
sys.path.append('E:/dog_breed_classification/LogisticRegressionModel/Shared/Shared.ReadData/Abstraction')
from AReadMongoDBImage import AReadMongoDBImage

class ReadMongoImage(AReadMongoDBImage):
    def __init__(self, uri, database_name):
        super().__init__(uri, database_name)
    
    
        
        




