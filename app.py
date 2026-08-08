from flask import Flask, request, jsonify, render_template
import joblib


# Create Flask application
app = Flask(__name__)


# Load the trained ML model
model = joblib.load("model/student_model.pkl")


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get data from the webpage
        data = request.get_json()

        # Get input values
        study_hours = float(data["study_hours"])
        attendance = float(data["attendance"])
        previous_score = float(data["previous_score"])
        assignments_completed = int(data["assignments_completed"])

        # Validate input values
        if study_hours < 0 or study_hours > 24:
            return jsonify({
                "error": "Study hours must be between 0 and 24."
            }), 400

        if attendance < 0 or attendance > 100:
            return jsonify({
                "error": "Attendance must be between 0 and 100."
            }), 400

        if previous_score < 0 or previous_score > 100:
            return jsonify({
                "error": "Previous score must be between 0 and 100."
            }), 400

        if assignments_completed < 0:
            return jsonify({
                "error": "Assignments cannot be negative."
            }), 400

        # Prepare data for ML model
        input_data = [[
            study_hours,
            attendance,
            previous_score,
            assignments_completed
        ]]

        # Make prediction
        prediction = model.predict(input_data)

        predicted_score = round(float(prediction[0]), 2)

        # Keep score between 0 and 100
        predicted_score = max(0, min(100, predicted_score))

        # Determine performance category
        if predicted_score >= 85:
            performance = "Excellent"
        elif predicted_score >= 70:
            performance = "Good"
        elif predicted_score >= 50:
            performance = "Average"
        else:
            performance = "Needs Improvement"

        # Return result
        return jsonify({
            "predicted_final_score": predicted_score,
            "performance": performance
        })

    except (KeyError, TypeError, ValueError):
        return jsonify({
            "error": "Please provide valid student information."
        }), 400


# Start Flask application
if __name__ == "__main__":
    app.run(debug=True)