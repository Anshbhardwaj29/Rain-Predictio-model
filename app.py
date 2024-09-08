import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Load the trained model
model_file_path = "Classifier.pkl"
model = pickle.load(open(model_file_path, "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data and check for None values
        humidity3pm = request.form.get('Humidity3pm')
        rain_today = request.form.get('RainToday')
        cloud3pm = request.form.get('Cloud3pm')
        humidity9am = request.form.get('Humidity9am')
        cloud9pm = request.form.get('Cloud9pm')
        rainfall = request.form.get('Rainfall')
        wind_gust_speed = request.form.get('WindGustSpeed')

        # Check if any required field is missing
        if None in [humidity3pm, rain_today, cloud3pm, humidity9am, cloud9pm, rainfall, wind_gust_speed]:
            return jsonify({"error": "All fields are required and must not be empty."})

        # Convert values to the correct type
        data = {
            "Humidity3pm": float(humidity3pm),
            "RainToday": int(rain_today),
            "Cloud3pm": float(cloud3pm),
            "Humidity9am": float(humidity9am),
            "Cloud9pm": float(cloud9pm),
            "Rainfall": float(rainfall),
            "WindGustSpeed": float(wind_gust_speed)
        }

        # Prepare features for prediction
        features = np.array(list(data.values())).reshape(1, -1)
        prediction = model.predict(features)

        # Convert the prediction to native Python type (0 or 1)
        prediction_result = int(prediction.item())

        # Check if rain is predicted
        if prediction_result == 1:
            message = "Rain will be there!"
        else:
            message = "No rain!"

        # Render the result page with the message
        return render_template("result.html", message=message)

    except Exception as e:
        # Return an error message if something goes wrong
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
