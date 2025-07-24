# app.py

from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form.get(feat)) for feat in [
            'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction',
            'high_blood_pressure', 'platelets', 'serum_creatinine', 'serum_sodium',
            'sex', 'smoking', 'time'
        ]]
        final_features = scaler.transform([features])
        prediction = model.predict(final_features)[0]
        result = "⚠️ High Risk of Heart Failure" if prediction == 1 else "✅ Low Risk of Heart Failure"
        return render_template("index.html", prediction_text=result)
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
