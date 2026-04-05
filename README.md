# 🩺 Diabetes Intelligence Platform

An AI-powered web application that predicts diabetes risk using Machine Learning. Built with **Flask**, trained on the **Pima Indians Diabetes Dataset**, and served through a modern, interactive dashboard.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-lightgrey?logo=flask)
![ML](https://img.shields.io/badge/ML-Gradient_Boosting-green)

---

## ✨ Features

- **🔐 Secure Login** — SQLite-backed authentication with hashed passwords (Werkzeug)
- **🤖 ML Prediction** — Gradient Boosting classifier (~78.5% accuracy) predicts diabetes risk from 8 health metrics
- **📊 Interactive Charts** — Chart.js visualizations for model comparison and glucose distribution
- **📄 PDF Reports** — One-click downloadable patient assessment reports via jsPDF
- **🎲 Random Test Cases** — Form auto-fills with one of 10 realistic sample cases on each page load
- **💎 Modern UI** — Glassmorphism design, gradient hero section, smooth animations, and responsive layout

---

## 📁 Project Structure

```
ML Project/
├── app.py                        # Flask server — routes, auth, and prediction logic
├── requirements.txt              # Python dependencies
├── README.md
├── .gitignore
│
├── data/
│   └── diabetes.csv             # Pima Indians Diabetes Dataset (768 samples, 8 features)
│
├── models/
│   ├── diabetes_model.pkl       # Trained Gradient Boosting model (serialized with pickle)
│   └── scaler.pkl               # StandardScaler fitted on training data
│
├── notebooks/
│   └── diabetes.ipynb           # Jupyter notebook — data analysis, model training, evaluation
│
├── database/
│   ├── force_create_db.py       # Script to initialize SQLite DB with a default admin user
│   └── users.db                 # SQLite database for user credentials
│
├── reports/
│   └── Diabetes prediction.pdf  # Sample generated report
│
├── static/
│   └── js/                      # Local JS libraries (Chart.js, Lucide Icons, jsPDF)
│
└── templates/
    ├── login.html               # Login page with glassmorphism card UI
    └── index.html               # Main dashboard — charts, prediction form, results
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.14+
- pip

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up the Database

Creates `database/users.db` with a default admin account:

```bash
python database/force_create_db.py
```

| Username | Password |
|----------|----------|
| `admin`  | `pass`   |

### 3. Run the Application

```bash
python app.py
```

The server starts at **http://127.0.0.1:5000**

---

## ⚙️ How It Works

1. **Login** → User authenticates via the login page (credentials checked against SQLite)
2. **Dashboard** → After login, the main page loads with interactive data charts
3. **Health Assessment** → User enters 8 health metrics (or uses a random test case)
4. **Prediction** → Form data is scaled using `StandardScaler` and fed to the trained model
5. **Result** → The prediction ("Diabetic" / "Not Diabetic") is displayed with an option to download a PDF report

### Input Features

| Feature | Description |
|---------|-------------|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose concentration (mg/dL) |
| Blood Pressure | Diastolic blood pressure (mm Hg) |
| Skin Thickness | Triceps skinfold thickness (mm) |
| Insulin | 2-hour serum insulin (mu U/ml) |
| BMI | Body mass index (kg/m²) |
| Diabetes Pedigree | Diabetes pedigree function score |
| Age | Age in years |

---

## 📊 Models Evaluated

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 75.3% |
| Random Forest | 77.1% |
| SVM | 76.2% |
| KNN | 73.8% |
| **Gradient Boosting** | **78.5%** 🏆 |

The **Gradient Boosting** classifier was selected as the final model.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Flask (Python) |
| ML Model | scikit-learn (Gradient Boosting) |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| Icons | Lucide |
| PDF Export | jsPDF |

---

## ⚠️ Disclaimer

This application is for **educational and demonstration purposes only**. It is **not** a medical diagnostic tool. Always consult a qualified healthcare professional for medical advice.