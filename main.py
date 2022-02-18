import json
import joblib

def iris_prediction(sepal_length, sepal_width, petal_length, petal_width):
    """
    Given sepal length, sepal width, petal length, and petal width,
    predict the class of iris
    """
    
    # Load the model from the file
    with open("model.pkl", "rb") as f:
        model = joblib.load(f)
        
    # Construct the 2D matrix of values that .predict is expecting
    X = [[sepal_length, sepal_width, petal_length, petal_width]]
    
    # Get a list of predictions and select only 1st
    predictions = model.predict(X)
    prediction = int(predictions[0])
    
    return {"predicted_class": prediction}

def predict(request):
    """
    `request` is an HTTP request object that will automatically be passed
    in by Google Cloud Functions
    
    You can find all of its properties and methods here:
    https://flask.palletsprojects.com/en/1.0.x/api/#flask.Request
    """
    # Get the request data from the user in JSON format
    request_json = request.get_json()
    
    # We are expecting the request to look like this:
    # {"sepal_length": <x1>, "sepal_width": <x2>, "petal_length": <x3>, "petal_width": <x4>}
    # Send it to our prediction function using ** to unpack the arguments
    result = iris_prediction(**request_json)
    
    # Return the result as a string with JSON format
    return json.dumps(result)
