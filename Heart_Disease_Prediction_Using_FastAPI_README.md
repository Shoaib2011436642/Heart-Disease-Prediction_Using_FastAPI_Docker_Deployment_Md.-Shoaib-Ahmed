
# Heart Disease Prediction Using FastAPI, Docker, and Machine Learning

### **Live Deployment**
Access the live app here:  
https://heart-disease-prediction-md-shoaib-ahmed.onrender.com/docs

---

### **Project Overview**

This project aims to develop a Heart Disease Prediction System trained using Machine Learning Model **Logistic Regression** and **FastAPI** for predicting heart disease based on health metrics such as age, cholesterol levels, and blood pressure. The model is deployed using **Docker** and **Render** for easy scaling and deployment.

---

### **Technologies Used**

- **FastAPI**: For building the web API.
- **Docker**: For containerizing the app.
- **scikit-learn**: For building the machine learning model.
- **joblib**: For saving and loading the trained model.
- **uvicorn**: For running the FastAPI app in production.

---

### **Purpose of the Project**

This project provides a tool for the **early detection of heart disease** using machine learning. By automating heart disease predictions, it aims to assist healthcare professionals in diagnosing patients faster.

---

### **How to Run Locally (Using Docker Desktop)**

1. Open **PowerShell** in your project folder.

2. Build and run the Docker container:
   ```bash
   docker-compose build
   docker-compose up
   ```

3. Open the app in your browser:
   - Go to `http://localhost:8000/docs` to interact with the API.

---

### **Deployment on Render**

The application is deployed on **Render** using Docker. The deployment steps include:
1. **Create a Render web service** and link it to the GitHub repository.
2. **Configure Docker** by setting the build context to `.` (root directory) and specifying the Dockerfile.
3. **Deploy** the application using Render’s **continuous deployment** feature, which rebuilds the app whenever changes are pushed to the GitHub repository.

The app is live and accessible via **Render's provided URL**, where you can interact with the API through Swagger UI.

---

### **Expected Result**

The app predicts whether a person is at risk for heart disease based on input features like age, cholesterol levels, and blood pressure. The result is returned as a **binary classification**.

---

### **Future Enhancements**

- Improve model accuracy.
- Integrate with real-time data for continuous monitoring.
