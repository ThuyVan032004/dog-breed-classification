import zope.interface
import numpy as np 
import seaborn as sns
from abc import ABC
import sys 

sys.path.append('E:/LogisticRegressionProject/LogisticRegression/Shared/Shared.Model/Model')
from ILogisticRegression import ILogisticRegression

@ zope.interface.implementer(ILogisticRegression)
class ALogisticRegression(ABC):
    def __init__(self, X, y):
        self.X = np.array(X)
        self.y = np.array(y)
            
