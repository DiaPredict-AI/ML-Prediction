from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import os
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)

# --- CONFIGURATION ---
# Get the directory where app.py is located to ensure we find files correctly
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "database", "users.db")
MODEL_FILE = os.path.join(BASE_DIR, "models", "diabetes_model.pkl")
SCALER_FILE = os.path.join(BASE_DIR, "models", "scaler.pkl")

# --- HELPER: Database Verification ---
def check_credentials(username, password):
    """
    Connects to SQLite DB and checks if username exists and password matches the hash.
    Returns True if valid, False otherwise.
    """
    if not os.path.exists(DB_NAME):
        print(f"Error: Database not found at {DB_NAME}")
        return False

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Fetch the password hash for the given username
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        user_record = cursor.fetchone()
        conn.close()

        if user_record:
            stored_hash = user_record[0]
            # Verify the provided password against the stored hash
            return check_password_hash(stored_hash, password)
        return False
    except Exception as e:
        print(f"Database Error: {e}")
        return False

# --- LOAD ML ARTIFACTS ---
model = None
scaler = None

if os.path.exists(MODEL_FILE):
    model = pickle.load(open(MODEL_FILE, "rb"))
else:
    print(f"Warning: Model file not found at {MODEL_FILE}")

if os.path.exists(SCALER_FILE):
    scaler = pickle.load(open(SCALER_FILE, "rb"))
else:
    print(f"Warning: Scaler file not found at {SCALER_FILE}")

# --- ROUTES ---

@app.route("/")
def login():
    """Serves the Login page."""
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    """Checks database for credentials before showing the dashboard."""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # --- NEW: DB CHECK ---
        if check_credentials(username, password):
            print(f"Login Successful for user: {username}")
            return render_template("index.html", username=username)
        else:
            print(f"Login Failed for user: {username}")
            return render_template("login.html", error="Invalid Username or Password")

    return redirect(url_for('login'))

@app.route("/predict", methods=["POST"])
def predict():
    if not model or not scaler:
        return render_template("index.html", prediction_text="Error: Model or Scaler file not found. Please check server logs.", username=request.form.get('username', ''))

    try:
        # Extract features from form
        features = [
            float(request.form['pregnancies']),
            float(request.form['glucose']),
            float(request.form['bp']),
            float(request.form['skinthickness']),
            float(request.form['insulin']),
            float(request.form['bmi']),
            float(request.form['dpf']),
            float(request.form['age'])
        ]

        # Scale the data (StandardScaler expects a 2D array)
        final_features = [np.array(features)]
        scaled_data = scaler.transform(final_features)
        
        # Predict
        prediction = model.predict(scaled_data)
        
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

        return render_template("index.html", prediction_text=result, username=request.form.get('username', ''))

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error processing data: {str(e)}", username=request.form.get('username', ''))

if __name__ == "__main__":
    print("Starting Flask Server...")
    # debug=False is better for final check
    app.run(debug=False)