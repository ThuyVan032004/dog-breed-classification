from sklearn.metrics import classification_report, confusion_matrix
import sys 
import seaborn as sns

sys.path.append('E:/dog_breed_classification/LogisticRegressionModel/Shared/Shared.Model/Abstraction')

from ALogisticRegression import ALogisticRegression

class TestLogisticRegression(ALogisticRegression):
    def __init__(self, model):
        self.model = model
    
    def predict(self, x_test):
        self.X_test = x_test
        return self.model.predict(self.X_test)
    
    def accuracyMeasurement(self, y_test, prediction):
        self.y_test = y_test
        sns.heatmap(confusion_matrix(self.y_test, prediction),annot=True,fmt="d")
        print(classification_report(self.y_test, prediction))
        