import sys 

# sys.path.append('../Shared/Shared.ProcessImage/Abstraction')
sys.path.append('E:/LogisticRegressionProject/LogisticRegression/Shared/Shared.ProcessImage/Abstraction')
from AProcessImage import AProcessImage

class ProcessImage(AProcessImage):
    def __init__(self, img_set):
        super().__init__(img_set)