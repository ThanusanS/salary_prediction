from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("finalized_model_linear.sav", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from frontend
        data = request.get_json()
        print("Received data:", data)

        # Convert input to float
        years = float(data["years"])

        # Convert to 2D array for sklearn
        features = np.array([[years]])

        # Make prediction
        prediction = model.predict(features)

        print("Raw prediction:", prediction)

        # Safely extract single value
        if isinstance(prediction, np.ndarray):
            prediction_value = prediction.item()
        else:
            prediction_value = prediction

        return jsonify({
            "prediction": round(float(prediction_value), 2)
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
