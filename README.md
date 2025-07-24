# 🫀 Heart Failure Prediction Web App

A Machine Learning-powered web application built with **Flask** that predicts the risk of heart failure based on key patient health metrics. This project aims to assist healthcare professionals and users in early identification of heart-related risks.

---

## 📌 Features

- 🔍 Predicts risk of heart failure based on clinical parameters.
- 💡 Trained ML model using real medical dataset (e.g., UCI Heart Failure Dataset).
- 🌐 Simple and interactive Flask-based web UI.
- 📊 Visualized performance metrics like accuracy, confusion matrix, etc.
- 🧠 Scalable: Easily replace or upgrade ML models (RandomForest, SVM, etc.).
- 💾 Model saved and loaded using `joblib`/`pickle`.

---

## 🧰 Tech Stack

| Layer       | Technologies Used                  |
|-------------|------------------------------------|
| Frontend    | HTML, CSS, Bootstrap               |
| Backend     | Python, Flask                      |
| ML Model    | Scikit-learn, Pandas, NumPy        |
| Deployment  | Flask App (Local or Cloud Hosting) |
| Optional    | Matplotlib / Seaborn for analysis  |

---

## 📂 Project Structure

heart_failure_app/
├── static/
│ └── styles.css # Optional custom styling
├── templates/
│ └── index.html # Main prediction form
│ └── result.html # Result display
├── model/
│ └── heart_model.pkl # Trained ML model
├── app.py # Flask app
├── requirements.txt # Python dependencies
└── README.md

markdown
Copy
Edit

---

## 📈 Dataset Used

- **Source:** UCI Heart Failure Prediction Dataset
- **Features Used:**
  - Age
  - Sex
  - Chest Pain Type
  - Resting Blood Pressure
  - Cholesterol
  - Fasting Blood Sugar
  - Rest ECG
  - Max Heart Rate
  - Exercise Induced Angina
  - ST Depression
  - Slope of ST
  - Number of Vessels Colored
  - Thal
- **Target:** Presence of heart disease (binary)
---


Screen Sort :

<img width="1920" height="1078" alt="Heart Failure Prediction - Google Chrome 22-07-2025 10_14_59" src="https://github.com/user-attachments/assets/55405cef-3970-41dd-8ebf-bf606bd4f0eb" />
<img width="1920" height="1078" alt="Heart Failure Prediction - Google Chrome 22-07-2025 10_15_06" src="https://github.com/user-attachments/assets/711fea7a-bd5e-431e-8a8f-cd82ac9d1b33" />




---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/heart_failure_app.git
cd heart_failure_app
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Flask application
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000/ in your browser.

🧠 ML Model Training (Optional)
If you want to retrain the model:

python
Copy
Edit
# train_model.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib

df = pd.read_csv("heart.csv")
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

joblib.dump(clf, "model/heart_model.pkl")
🧪 Sample Input Fields
Field	Type
Age	int
Sex (0 = F, 1 = M)	int
Chest Pain Type (0–3)	int
Resting BP	float
Cholesterol	float
Fasting Blood Sugar	int
Rest ECG (0–2)	int
Max Heart Rate Achieved	int
Exercise Induced Angina	int
ST Depression	float
Slope of ST	int
Vessels Colored (0–3)	int
Thal (1, 2, 3)	int

📊 Model Accuracy
Accuracy: ~85%

Model: Random Forest Classifier (or best performing model)

Evaluation Metrics: Confusion Matrix, ROC AUC Score


🏁 Future Improvements
✅ Deploy on Render/Heroku/Streamlit Cloud.

✅ Add authentication system.

✅ Visual analytics and charts.

✅ Store patient predictions using SQLite/PostgreSQL.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

📜 License
This project is licensed under the MIT License.

📧 Contact
Created by Your Name • Email: your.email@example.com

yaml
Copy
Edit

---

Would you like this README customized with your **GitHub username**, **dataset**, or **deployment method (e.g., Streamlit, Heroku)**?







