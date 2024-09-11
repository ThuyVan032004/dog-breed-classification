import joblib 
from Reader.ReadMongoImageDog import ReadMongoImage
from ProcessImage.ProcessImageDog import ProcessImage
from Train.TrainDog import TrainLogisticRegression
from Test.TestDog import TestLogisticRegression

def trainModel():
    uri = 'mongodb+srv://magift:dothithuyvan3081@crawler-demo.7205a.mongodb.net/'
    database_name = 'crawler-demo'
    reader = ReadMongoImage(uri, database_name)
    X, y = reader.readData()
    image_processor = ProcessImage(X)
    image_processor.resize(150, 150)
    image_processor.flattenImage()
    X = image_processor.img_set
    trainer = TrainLogisticRegression(X, y)
    trainer.trainModel()
    tester = TestLogisticRegression(trainer.model)
    tester.predict(trainer.X_test)
    tester.accuracyMeasurement(trainer.y_test)
    joblib.dump(tester, "TrainDog.joblib")