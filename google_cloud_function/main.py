import pickle
import json
from flask import abort

def predict_wine(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # Get the request from the user
    request_json = request.get_json()
    expected_features = ("Alcohol", "Malic acid", "Ash", "Alcalinity of ash", \
        "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", \
        "Proanthocyanins", "Color intensity", "Hue", \
        "OD280/OD315 of diluted wines", "Proline")

    # Check to make sure all of the necessary fields are present
    if request_json and all(feature in request_json for feature in expected_features):

        # Convert the dict of fields into a list
        test_value = [request_json[feature] for feature in expected_features]

        # Load the model from the .pickle file
        model_file = open("wine_classifier.pickle", "rb")
        loaded_model = pickle.load(model_file)
        model_file.close()

        # Make a prediction based on the user's request
        predicted_class = int(loaded_model.predict([test_value])[0])

        # Construct a response and return it
        response_json = {"prediction": predicted_class}
        return json.dumps(response_json)
    else:
        return abort(400)
