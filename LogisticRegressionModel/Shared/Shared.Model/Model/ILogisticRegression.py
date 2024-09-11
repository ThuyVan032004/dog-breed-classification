import zope.interface

class ILogisticRegression(zope.interface.Interface):
    def trainModel(self):
        pass
    def predict(self, x_test):
        pass
    def accuracyMeasurement(self, y_test, prediction):
        pass 