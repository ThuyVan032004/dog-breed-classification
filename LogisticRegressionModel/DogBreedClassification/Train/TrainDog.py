from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import sys 

sys.path.append('E:/dog_breed_classification/LogisticRegressionModel/Shared/Shared.Model/Abstraction')
from ALogisticRegression import ALogisticRegression

class TrainLogisticRegression(ALogisticRegression):
    def __init__(self, X, y):
        super().__init__(X, y)
        self.model = LogisticRegression()

    def trainModel(self):
        X_train,self.X_test,y_train,self.y_test=train_test_split(self.X, self.y, test_size=0.1, random_state=0)       
        self.model.fit(X_train, y_train)

