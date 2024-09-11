import joblib 
import sys
import json
from ProcessImage.ProcessImageDog import ProcessImage
from Reader.ReadClientImageDog import ReadClientImage

def application(img_url):
    reader = ReadClientImage(image_url=img_url)
    X = reader.readData()
    image_processor = ProcessImage(X)
    image_processor.resize(150, 150)
    image_processor.flattenImage()
    X = image_processor.img_set
    model = joblib.load("E:/LogisticRegressionProject/LogisticRegression/DogBreedClassification/TrainDog.joblib")
    prediction = int(model.predict(X)[0])
    return prediction

if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_url = sys.argv[1]
        result = application(img_url)
        print(json.dumps({"result": result}))
    else:
        print(json.dumps({"error": "No image URL provided"}))