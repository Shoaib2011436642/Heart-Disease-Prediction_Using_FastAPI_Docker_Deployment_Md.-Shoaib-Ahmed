from fastapi import FastAPI
from app.schemas import HeartDiseaseInput  # Correct import path
import joblib

# Load the trained model
try:
    model = joblib.load('/model/heart_model.joblib')
except Exception as e:
    print(f"Error loading model: {e}")

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/info")
def info():
    return {
        "model_type": "Logistic Regression",
        "features": ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
    }

@app.post("/predict")
def predict(input_data: HeartDiseaseInput):
    # Convert input data into a feature vector
    input_vector = [[
        input_data.age, input_data.sex, input_data.cp, input_data.trestbps, input_data.chol, 
        input_data.fbs, input_data.restecg, input_data.thalach, input_data.exang, input_data.oldpeak,
        input_data.slope, input_data.ca, input_data.thal
    ]]

    # Predict heart disease
    prediction = model.predict(input_vector)

    return {"heart_disease": bool(prediction[0])}
