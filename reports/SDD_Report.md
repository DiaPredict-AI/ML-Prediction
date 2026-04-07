# SOFTWARE DESIGN DOCUMENT (SDD)

# Diabetes Intelligence Platform

**An AI-Powered Diabetes Risk Prediction Web Application**

---

| Field               | Details                                    |
|---------------------|--------------------------------------------|
| **Project Title**   | Diabetes Intelligence Platform             |
| **Document Type**   | Software Design Document (SDD)             |
| **Version**         | 1.0                                        |
| **Date**            | April 06, 2026                             |
| **Technology Stack**| Python, Flask, scikit-learn, SQLite, HTML/CSS/JS |
| **Dataset**         | Pima Indians Diabetes Dataset (768 records)|

---

## Table of Contents

| Section | Title | Page |
|---------|-------|------|
| — | Abstract | 6 |
| 1 | Introduction | 7 |
| 1.1 | Project Objectives | 9 |
| 1.2 | Project Goals | 9 |
| 1.3 | Scope | 10 |
| 1.4 | Definitions & Acronyms | 10 |
| 2 | System Requirements | 11 |
| 2.1 | Hardware Requirements | 11 |
| 2.2 | Software Requirements | 11 |
| 3 | Requirement Analysis | 12 |
| 3.1 | Functional Requirements | 12 |
| 3.2 | Non-functional Requirements | 12 |
| 4 | Data Design & Modelling | 13 |
| 4.1 | User Diagram | 13 |
| 4.2 | ERD (Entity Relationship Diagram) | 13 |
| 4.3 | Object Diagram | 14 |
| 4.4 | Data Dictionary | 15 |
| 5 | System Design | 16 |
| 5.1 | Class Diagram | 16 |
| 5.2 | Component Diagram | 17 |
| 6 | Behavioral Design | 19 |
| 6.1 | Activity Diagram | 19 |
| 6.2 | Sequence Diagram | 20 |
| 6.3 | Collaboration Diagram | 21 |
| 7 | Implementation & Physical Design | 22 |
| 7.1 | Deployment Diagram | 22 |
| 7.2 | Interface Design & UX | 22 |
| 8 | Data Analysis & Insights | 24 |
| 8.1 | Analysis Methodology | 24 |
| 8.2 | Visualization Gallery | 24 |
| 9 | Gallery | 25 |
| 10 | Testing & Quality Assurance | 28 |
| 10.1 | Test Cases | 28 |
| 10.2 | Browser/Device Compatibility | 28 |
| 11 | Maintenance & Future Scope | 29 |
| 12 | Conclusion & References | 30 |
| 12.1 | Project Limitations | 31 |
| 12.2 | Future Scope | 32 |
| 12.3 | Results | 33 |

---

## Abstract

The **Diabetes Intelligence Platform** is a full-stack, AI-powered web application developed using Python and the Flask micro-framework. The primary purpose of this system is to provide an accessible, real-time tool for predicting the likelihood of diabetes in a patient based on eight clinically relevant health metrics. The application integrates a machine learning model trained on the well-established **Pima Indians Diabetes Dataset** — a benchmark dataset comprising 768 patient records collected by the National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK).

The system pipeline begins with a structured data analysis and model training phase conducted in a Jupyter Notebook environment. Five classification algorithms were evaluated: Logistic Regression, Random Forest, Support Vector Machine (SVM), K-Nearest Neighbors (KNN), and Gradient Boosting. The **Gradient Boosting classifier** was selected as the final model, achieving a peak accuracy of **78.5%**, the highest among all candidates.

The trained model and its corresponding `StandardScaler` preprocessor are serialized using Python's `pickle` module and loaded dynamically into the Flask server at runtime. A robust **SQLite-backed user authentication** system protects access to the prediction dashboard, using **PBKDF2-SHA256** password hashing with 260,000 iterations for security.

The frontend is built with HTML, CSS, and JavaScript, featuring a **glassmorphism-inspired UI** with interactive Chart.js visualizations, a one-click PDF report generation feature (via jsPDF), and a random test-case auto-fill functionality to aid demonstration. This document serves as the complete Software Design Document (SDD) for the platform, covering all design, architecture, data modelling, behavioral flows, testing procedures, and future enhancement roadmaps.

> **Disclaimer:** This application is intended strictly for **educational and demonstration purposes**. It does not constitute or replace qualified medical advice.

---

## 1. Introduction

### 1.1 Background

Diabetes mellitus is one of the fastest-growing chronic diseases globally. According to the International Diabetes Federation (IDF), over 537 million adults were living with diabetes in 2021, with projections estimating this number will rise to 783 million by 2045. Early detection and risk assessment are critical to prevent complications such as cardiovascular disease, kidney failure, and neuropathy.

Traditional clinical screening relies on lab tests and physician consultations, which can be inaccessible in resource-constrained environments. Machine learning offers a powerful alternative — using statistical patterns learned from historical patient data to generate risk predictions quickly, economically, and at scale.

### 1.2 Problem Statement

A significant portion of the global population remains undiagnosed or receives a late-stage diabetes diagnosis due to:
- Limited access to healthcare professionals in rural or low-income areas
- High cost of routine diagnostic tests
- Lack of awareness of early warning symptoms

There is a need for a **lightweight, intelligent, and user-friendly digital tool** that can provide a preliminary diabetes risk assessment based on simple health metrics, helping bridge the gap between population health and clinical diagnosis.

### 1.3 Motivation

This project was motivated by the following factors:
1. **Educational value** — to demonstrate end-to-end machine learning deployment in a web application context.
2. **Medical relevance** — to apply data science to a real-world health problem with measurable social impact.
3. **Technical challenge** — to integrate a trained ML model with a secure web backend and a polished frontend in a cohesive full-stack system.

### 1.4 Project Overview

The Diabetes Intelligence Platform is structured as a three-tier web application:

| Tier | Component | Technology |
|------|-----------|------------|
| **Presentation** | UI / Dashboard | HTML, CSS, JavaScript, Chart.js, jsPDF |
| **Application Logic** | Web Server + ML Engine | Python 3.14, Flask |
| **Data** | User Auth + ML Artifacts | SQLite, Pickle (.pkl) |

The application accepts eight patient health parameters as input, scales the data using a pre-fitted `StandardScaler`, and feeds it to a trained `GradientBoostingClassifier` to return a binary prediction: **"Diabetic"** or **"Not Diabetic"**.

---

## 1.1 Project Objectives

The primary objectives of the Diabetes Intelligence Platform are:

1. **Develop a predictive ML model** capable of classifying diabetes risk based on eight key physiological parameters with a target accuracy above 75%.

2. **Deploy the model as a web service** using Flask, making it accessible via any modern web browser without requiring local installation by the end user.

3. **Implement secure user authentication** using hashed password storage to ensure that only authorized personnel can access the prediction dashboard.

4. **Design a professional and intuitive user interface** incorporating data visualization charts, responsive layouts, and accessibility-focused UX patterns.

5. **Generate downloadable patient assessment reports** in PDF format directly from the browser using client-side JavaScript libraries.

6. **Document the complete software lifecycle** from data analysis and model selection through to deployment, testing, and future enhancement planning.

---

## 1.2 Project Goals

| # | Goal | Success Metric |
|---|------|----------------|
| G1 | Train an accurate diabetes classifier | ≥ 78% accuracy on test set |
| G2 | Serve predictions via a web API | < 500ms average response time |
| G3 | Secure user login system | PBKDF2-SHA256 with 260,000 iterations |
| G4 | Interactive data visualization dashboard | Min. 2 interactive charts (Chart.js) |
| G5 | PDF report generation | One-click export with jsPDF |
| G6 | Responsive UI across screen sizes | Compatible on desktops, tablets, mobile |
| G7 | Modular, maintainable codebase | Separate concerns: model, routes, DB, templates |

---

## 1.3 Scope

### In Scope

- Binary classification of diabetes risk (Diabetic / Not Diabetic)
- User authentication (login/logout) backed by a local SQLite database
- Flask-based REST-like web server with defined routes (`/`, `/dashboard`, `/predict`)
- Data preprocessing with `StandardScaler` before prediction
- Frontend dashboard with embedded charts and a health metrics input form
- PDF report generation on the client side
- Random test-case population for demonstration
- Documentation covering all SDD phases

### Out of Scope

- Multi-user registration and account management (only a pre-seeded admin account is supported)
- Real-time integration with electronic health records (EHR) systems
- Mobile native application (iOS / Android)
- Role-based access control (RBAC)
- Cloud deployment or containerization (Docker/Kubernetes)
- Real-time data streaming or continuous model re-training

---

## 1.4 Definitions & Acronyms

| Term / Acronym | Definition |
|----------------|------------|
| **SDD** | Software Design Document |
| **ML** | Machine Learning |
| **GBC** | Gradient Boosting Classifier |
| **API** | Application Programming Interface |
| **Flask** | A lightweight Python WSGI micro web framework |
| **SQLite** | A serverless, file-based relational database engine |
| **PBKDF2** | Password-Based Key Derivation Function 2 — a key stretching algorithm |
| **SHA-256** | Secure Hash Algorithm 256-bit, a cryptographic hash function |
| **pkl / Pickle** | Python serialization format for persisting objects |
| **StandardScaler** | scikit-learn transformer that standardizes features (zero mean, unit variance) |
| **ERD** | Entity Relationship Diagram |
| **UML** | Unified Modeling Language |
| **HTML** | HyperText Markup Language |
| **CSS** | Cascading Style Sheets |
| **JS** | JavaScript |
| **jsPDF** | A JavaScript library for generating PDFs in the browser |
| **Chart.js** | A JavaScript charting library for interactive data visualizations |
| **BMI** | Body Mass Index |
| **DPF** | Diabetes Pedigree Function |
| **NIDDK** | National Institute of Diabetes and Digestive and Kidney Diseases |
| **IDF** | International Diabetes Federation |
| **ROC** | Receiver Operating Characteristic (curve) |
| **AUC** | Area Under the ROC Curve |
| **UI/UX** | User Interface / User Experience |
| **WSGI** | Web Server Gateway Interface |

---

## 2. System Requirements

### 2.1 Hardware Requirements

| Component | Minimum Specification | Recommended Specification |
|-----------|-----------------------|---------------------------|
| **Processor** | Intel Core i3 / AMD Ryzen 3 (2.0 GHz) | Intel Core i5 / AMD Ryzen 5 (2.4 GHz+) |
| **RAM** | 4 GB | 8 GB |
| **Storage** | 500 MB free disk space | 2 GB free disk space |
| **Display** | 1280 x 720 resolution | 1920 x 1080 resolution |
| **Network** | Not required for local deployment | Broadband for hosted deployment |
| **GPU** | Not required (CPU inference) | N/A |

### 2.2 Software Requirements

| Category | Requirement | Version / Notes |
|----------|-------------|-----------------|
| **Operating System** | Windows 10/11, macOS 12+, Ubuntu 20.04+ | Cross-platform |
| **Runtime** | Python | 3.14+ |
| **Package Manager** | pip | Bundled with Python |
| **Web Framework** | Flask | 3.x |
| **ML Library** | scikit-learn | 1.5+ |
| **Numerical Computing** | NumPy | 1.26+ |
| **Data Processing** | Pandas | 2.x |
| **Database** | SQLite3 | Built into Python stdlib |
| **Serialization** | pickle | Built into Python stdlib |
| **Web Browser** | Chrome 110+, Firefox 110+, Edge 110+ | For the frontend UI |
| **Development Tools** | VS Code, Jupyter Notebook | Optional but recommended |
| **Version Control** | Git | 2.x |

**Python Dependency File (`requirements.txt`):**

```
Flask
scikit-learn
numpy
pandas
```

---

## 3. Requirement Analysis

### 3.1 Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| **FR-01** | The system shall present a login page as the entry point (`/`) | High |
| **FR-02** | The system shall validate user credentials against the SQLite `users` table | High |
| **FR-03** | Valid credentials shall redirect the user to the main dashboard (`/dashboard`) | High |
| **FR-04** | Invalid credentials shall return the user to the login page with an error message | High |
| **FR-05** | The dashboard shall display at least two interactive data visualization charts | Medium |
| **FR-06** | The system shall render a health metrics input form with 8 fields | High |
| **FR-07** | On form submission to `/predict`, the system shall scale input data using `StandardScaler` | High |
| **FR-08** | The scaled data shall be fed to the `GradientBoostingClassifier` for binary prediction | High |
| **FR-09** | The prediction result ("Diabetic" / "Not Diabetic") shall be displayed on the dashboard | High |
| **FR-10** | Each page load shall auto-fill the form with a randomly selected test case | Low |
| **FR-11** | The user shall be able to generate and download a PDF assessment report | Medium |
| **FR-12** | Passwords shall be stored as PBKDF2-SHA256 hashes; plaintext passwords shall never be stored | High |
| **FR-13** | The system shall gracefully handle missing model or scaler files with an appropriate error | Medium |

### 3.2 Non-functional Requirements

| ID | Requirement | Category | Target |
|----|-------------|----------|--------|
| **NFR-01** | Prediction response time shall be under 500ms for local deployment | Performance | < 500ms |
| **NFR-02** | The UI shall be responsive and functional on screen widths from 360px to 2560px | Usability | Responsive |
| **NFR-03** | Password hashing shall use PBKDF2-SHA256 with a minimum of 260,000 iterations | Security | PBKDF2-SHA256 |
| **NFR-04** | Salt for each password hash shall be cryptographically random (16-byte hex) | Security | `secrets.token_hex(16)` |
| **NFR-05** | The application shall remain functional if charts fail to load (graceful degradation) | Reliability | No crash |
| **NFR-06** | The codebase shall be organized into distinct modules: routes, DB, templates, models | Maintainability | Separation of concerns |
| **NFR-07** | The application shall not require an internet connection to run in local mode | Portability | Offline-capable |
| **NFR-08** | Chart.js, Lucide Icons, and jsPDF shall be served as local static assets | Portability | No CDN dependency |
| **NFR-09** | Model accuracy shall be >= 75% on the test split of the Pima dataset | Quality | >= 75% accuracy |
| **NFR-10** | All SQL queries shall use parameterized statements to prevent SQL injection | Security | Parameterized queries |

---

## 4. Data Design & Modelling

### 4.1 User Diagram

[User Diagram]

_The user diagram illustrates the two primary actor types interacting with the system: the **Administrator** (authenticated user who accesses the dashboard and triggers predictions) and the **System** (Flask server + ML engine + SQLite database). The administrator interacts via the browser, while the system processes requests internally._

---

### 4.2 ERD (Entity Relationship Diagram)

[ERD Diagram]

**Entities and Attributes:**

**Entity: `users`**

| Attribute | Type | Constraints |
|-----------|------|-------------|
| `id` | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| `username` | TEXT | UNIQUE, NOT NULL |
| `password_hash` | TEXT | NOT NULL |

**Entity: `prediction_session` (Logical / In-Memory)**

| Attribute | Type | Description |
|-----------|------|-------------|
| `username` | TEXT | Logged-in user identifier |
| `pregnancies` | FLOAT | Number of pregnancies |
| `glucose` | FLOAT | Plasma glucose level (mg/dL) |
| `bp` | FLOAT | Diastolic blood pressure (mm Hg) |
| `skin_thickness` | FLOAT | Triceps skinfold (mm) |
| `insulin` | FLOAT | 2-hour serum insulin (mu U/ml) |
| `bmi` | FLOAT | Body mass index (kg/m2) |
| `dpf` | FLOAT | Diabetes pedigree function |
| `age` | FLOAT | Age in years |
| `result` | TEXT | "Diabetic" or "Not Diabetic" |

> **Note:** Prediction sessions are not persisted to the database in the current version. They are handled transiently within the Flask request-response cycle.

**Relationships:**

- A `user` may initiate zero or more `prediction_sessions` (one-to-many, logical)
- The `users` table is the sole persistent entity in the SQLite database

---

### 4.3 Object Diagram

[Object Diagram]

**Runtime Object Snapshot (Sample Prediction Execution):**

```
FlaskApp
  MODEL_FILE = "models/diabetes_model.pkl"
  DB_NAME    = "database/users.db"
  model      = GradientBoostingClassifier(...)
  scaler     = StandardScaler(...)

GradientBoostingClassifier
  n_estimators  = 100
  learning_rate = 0.1

StandardScaler
  mean_  = [3.8, 120.9, ...]
  scale_ = [3.4, 31.9, ...]

PredictionRequest
  pregnancies    = 6.0
  glucose        = 148.0
  bp             = 72.0
  skin_thickness = 35.0
  insulin        = 0.0
  bmi            = 33.6
  dpf            = 0.627
  age            = 50.0

PredictionResult
  result = "Diabetic"
```

---

### 4.4 Data Dictionary

#### Dataset: `diabetes.csv` (Pima Indians Diabetes Dataset)

| Column | Data Type | Range | Unit | Description |
|--------|-----------|-------|------|-------------|
| `Pregnancies` | Integer | 0 - 17 | Count | Number of times pregnant |
| `Glucose` | Integer | 0 - 199 | mg/dL | Plasma glucose concentration (2-hour oral glucose tolerance test) |
| `BloodPressure` | Integer | 0 - 122 | mm Hg | Diastolic blood pressure |
| `SkinThickness` | Integer | 0 - 99 | mm | Triceps skinfold thickness |
| `Insulin` | Integer | 0 - 846 | mu U/ml | 2-hour serum insulin |
| `BMI` | Float | 0 - 67.1 | kg/m2 | Body mass index |
| `DiabetesPedigreeFunction` | Float | 0.078 - 2.420 | Score | Genetic predisposition score |
| `Age` | Integer | 21 - 81 | Years | Age of patient |
| `Outcome` | Integer | 0 or 1 | Binary | Target label: 1 = Diabetic, 0 = Not Diabetic |

**Dataset Statistics:**

| Statistic | Pregnancies | Glucose | BloodPressure | BMI | Age |
|-----------|-------------|---------|----------------|-----|-----|
| Count | 768 | 768 | 768 | 768 | 768 |
| Mean | 3.85 | 120.89 | 69.11 | 31.99 | 33.24 |
| Std Dev | 3.37 | 31.97 | 19.36 | 7.88 | 11.76 |
| Min | 0 | 0 | 0 | 0 | 21 |
| Max | 17 | 199 | 122 | 67.1 | 81 |

#### Schema: `database/users.db` — Table: `users`

| Column | Data Type | Constraint | Example Value |
|--------|-----------|------------|---------------|
| `id` | INTEGER | PRIMARY KEY, AUTOINCREMENT | `1` |
| `username` | TEXT | UNIQUE, NOT NULL | `"admin"` |
| `password_hash` | TEXT | NOT NULL | `"pbkdf2_sha256$260000$abc123$..."` |

**Password Hash Format:**
```
pbkdf2_sha256 $ {iterations} $ {salt_hex} $ {hash_hex}
```

---

## 5. System Design

### 5.1 Class Diagram

[Class Diagram]

**Key Classes and Responsibilities:**

```
FlaskApp
  Attributes:
    BASE_DIR: str
    DB_NAME: str
    MODEL_FILE: str
    SCALER_FILE: str
    model: GradientBoostingClassifier
    scaler: StandardScaler
  Methods:
    login() -> Response
    dashboard() -> Response
    predict() -> Response

AuthService
  Attributes:
    DB_NAME: str
  Methods:
    verify_password(stored_hash, password) -> bool
    check_credentials(username, password) -> bool

MLInferenceService
  Attributes:
    model: GradientBoostingClassifier
    scaler: StandardScaler
  Methods:
    preprocess(features: list) -> ndarray
    predict(scaled_data: ndarray) -> int

HealthMetricsInput
  Attributes:
    pregnancies: float
    glucose: float
    bp: float
    skinthickness: float
    insulin: float
    bmi: float
    dpf: float
    age: float
```

---

### 5.2 Component Diagram

[Component Diagram]

**Component Breakdown:**

| Component | Responsibility | Files |
|-----------|---------------|-------|
| **Frontend (Browser)** | Render UI, capture inputs, display results, generate PDFs | `login.html`, `index.html`, `static/js/` |
| **Flask Backend** | Route handling, request/response orchestration | `app.py` |
| **Auth Module** | Credential verification using PBKDF2-SHA256 | `app.py` (verify_password, check_credentials) |
| **ML Engine** | Feature scaling + model inference | `app.py` (predict route) + `.pkl` files |
| **Data Layer** | Persistent user storage + serialized ML artifacts | `users.db`, `diabetes_model.pkl`, `scaler.pkl` |
| **Training Pipeline** | Offline EDA, model training, export | `notebooks/diabetes.ipynb` |

**Component Interfaces:**

| From | To | Interface | Data |
|------|----|-----------|------|
| Browser (login.html) | Flask `/dashboard` | HTTP POST | `username`, `password` |
| Flask `/dashboard` | AuthService | Function call | `username`, `password` |
| AuthService | SQLite `users.db` | SQL SELECT | `username` -> `password_hash` |
| Browser (index.html) | Flask `/predict` | HTTP POST | 8 health metric fields |
| Flask `/predict` | MLInferenceService | Function call | `features[]` |
| MLInferenceService | scaler.pkl | `transform()` | Raw feature vector |
| MLInferenceService | diabetes_model.pkl | `predict()` | Scaled feature vector |
| Flask `/predict` | Browser (index.html) | HTTP Response | `prediction_text` string |

---

## 6. Behavioral Design

### 6.1 Activity Diagram

[Activity Diagram]

**Main Flow: Login -> Predict -> Report**

```
[START]
  |
  v
User navigates to http://127.0.0.1:5000/
  |
  v
Login Page Rendered
  |
  v
User enters username + password -> Submit (POST /dashboard)
  |
  |--[Credentials Valid? YES]---> Render dashboard (index.html)
  |                                         |
  |--[NO]---> Render login.html             v
              with error msg      User views charts + form
                                            |
                                            v
                                  User enters 8 health metrics
                                  (or uses random test case)
                                            |
                                            v
                                  Submit form -> POST /predict
                                            |
                                            v
                                  StandardScaler.transform()
                                            |
                                            v
                                  GBC.predict()
                                            |
                                            v
                                  Result displayed on dashboard
                                            |
                                            v
                                  [Optional] Download PDF Report
                                            |
                                            v
                                         [END]
```

---

### 6.2 Sequence Diagram

[Sequence Diagram]

**Sequence: Health Metrics Prediction Request**

```
Actor         Browser          Flask (app.py)      AuthService     MLEngine     DB (users.db)
               |                   |                   |              |               |
               |--POST /dashboard->|                   |              |               |
               |  (username, pw)   |                   |              |               |
               |                   |--check_cred()---->|              |               |
               |                   |                   |--SELECT user---------------->|
               |                   |                   |<--user_record (pw_hash)------|
               |                   |                   |--verify_pass()               |
               |                   |                   |  (PBKDF2-SHA256)             |
               |                   |<--True/False------|              |               |
               |<--render index.html (if valid)        |              |               |
               |                   |                   |              |               |
               |--POST /predict--->|                   |              |               |
               |  (8 features)     |---preprocess()---------------------------------->|
               |                   |                   |   scaler.transform()         |
               |                   |<--scaled_data----------------------              |
               |                   |---predict()----------------------------->        |
               |                   |                   |   GBC.predict()              |
               |                   |<--[0] or [1]------|              |               |
               |<--render result---|                   |              |               |
               |  prediction_text  |                   |              |               |
```

---

### 6.3 Collaboration Diagram

[Collaboration Diagram]

**Object Collaboration: Prediction Workflow**

```
1: POST /predict(features)
   Browser --------> FlaskApp

2: preprocess(features)
   FlaskApp --------> StandardScaler

3: return scaled_data
   StandardScaler --------> FlaskApp

4: predict(scaled_data)
   FlaskApp --------> GradientBoostingClassifier

5: return prediction [0 or 1]
   GradientBoostingClassifier --------> FlaskApp

6: render_template("index.html", prediction_text=result)
   FlaskApp --------> Browser

7: [Optional] generatePDF()
   Browser --------> jsPDF (Client-side, no server round-trip)
```

---

## 7. Implementation & Physical Design

### 7.1 Deployment Diagram

[Deployment Diagram]

**Local Deployment Configuration:**

```
Developer Workstation
  OS: Windows 10/11 / macOS / Ubuntu
  Python 3.14+

  Flask Development Server
    Host: 127.0.0.1   Port: 5000
    WSGI: Werkzeug (built-in)

    app.py              (Routes + Logic)
    models/
      diabetes_model.pkl
      scaler.pkl
    database/
      users.db (SQLite)
    templates/
      login.html
      index.html
    static/js/
      chart.js
      lucide.js
      jspdf.js

  <--- HTTP (localhost) --->

  Web Browser (Chrome/Firefox/Edge)
    http://127.0.0.1:5000
```

**File System Layout:**

```
ML Project/
├── app.py                       <- Entry point
├── requirements.txt             <- Dependencies
├── README.md
├── .gitignore
├── data/
│   └── diabetes.csv             <- Raw training data (768 samples, 9 columns)
├── models/
│   ├── diabetes_model.pkl       <- Serialized GBC model
│   └── scaler.pkl               <- Serialized StandardScaler
├── notebooks/
│   └── diabetes.ipynb           <- EDA + model training
├── database/
│   ├── force_create_db.py       <- DB initialization script
│   └── users.db                 <- SQLite user database
├── reports/
│   └── Diabetes prediction.pdf  <- Sample PDF output
├── static/
│   └── js/                      <- Offline JS libraries
└── templates/
    ├── login.html               <- Authentication UI
    └── index.html               <- Main dashboard
```

---

### 7.2 Interface Design & UX

#### Login Page (`/`)

**Design Concept:** Glassmorphism card centered on a gradient background.

| Element | Description |
|---------|-------------|
| Background | Deep blue-purple gradient |
| Card style | Frosted glass effect with backdrop blur |
| Logo/Brand | Stethoscope icon + "Diabetes Intelligence Platform" heading |
| Username field | Rounded input with Lucide icon |
| Password field | Masked input with show/hide toggle |
| Submit button | Gradient CTA button with hover animation |
| Error message | Inline red alert displayed on authentication failure |

[Login Page Screenshot]

---

#### Dashboard Page (`/dashboard` -> `index.html`)

**Design Concept:** Full-featured health analytics dashboard with glassmorphism aesthetic.

| Section | Description |
|---------|-------------|
| **Hero / Header** | Gradient banner with welcome message, username display, tagline |
| **Info Cards Row** | Three metric cards: Total Records (768), Features Used (8), Model Accuracy (78.5%) |
| **Chart Section** | Two side-by-side Chart.js charts: Model Accuracy Comparison + Glucose Distribution |
| **Prediction Form** | 8 labeled inputs arranged in a 2-column grid with range hints |
| **Random Test Case** | Auto-populated on each page load with one of 10 realistic sample cases |
| **Result Display** | Color-coded result card — green for "Not Diabetic", red for "Diabetic" |
| **PDF Export** | "Download Report" button triggers client-side jsPDF PDF generation |
| **Footer** | Disclaimer and project attribution |

[Dashboard Screenshot]

---

**Input Form Fields:**

| Field Label | HTML name | Type | Example Value |
|-------------|-----------|------|---------------|
| Number of Pregnancies | `pregnancies` | Number | `6` |
| Glucose Level (mg/dL) | `glucose` | Number | `148` |
| Blood Pressure (mm Hg) | `bp` | Number | `72` |
| Skin Thickness (mm) | `skinthickness` | Number | `35` |
| Insulin Level (mu U/ml) | `insulin` | Number | `0` |
| BMI (kg/m2) | `bmi` | Number | `33.6` |
| Diabetes Pedigree Function | `dpf` | Number | `0.627` |
| Age (years) | `age` | Number | `50` |

---

## 8. Data Analysis & Insights

### 8.1 Analysis Methodology

The data analysis and model development were conducted in the Jupyter Notebook (`notebooks/diabetes.ipynb`) and followed this standard ML pipeline:

#### Step 1: Data Loading & Inspection
- Loaded `diabetes.csv` using Pandas
- Inspected shape (768 rows x 9 columns), data types, and null values
- Checked class distribution: **268 Diabetic (34.9%)** vs **500 Non-Diabetic (65.1%)**

#### Step 2: Exploratory Data Analysis (EDA)
- **Descriptive statistics** — mean, std, min/max for all features
- **Zero-value analysis** — Glucose, BloodPressure, SkinThickness, Insulin, and BMI contained zeros representing missing data
- **Correlation heatmap** — Glucose (0.47), BMI (0.29), and Age (0.24) showed the strongest positive correlation with Outcome

#### Step 3: Preprocessing
- **Zero imputation** — Replaced biologically impossible zeros with column medians
- **Feature scaling** — Applied `StandardScaler.fit_transform()` on the training split only to prevent data leakage

#### Step 4: Train/Test Split
- 80% Training / 20% Test split using `train_test_split(random_state=42)`
- Training samples: **614** | Test samples: **154**

#### Step 5: Model Training & Evaluation

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 75.3% | 0.72 | 0.60 | 0.66 |
| Random Forest | 77.1% | 0.74 | 0.64 | 0.69 |
| SVM | 76.2% | 0.73 | 0.62 | 0.67 |
| KNN | 73.8% | 0.70 | 0.58 | 0.64 |
| **Gradient Boosting** | **78.5%** | **0.76** | **0.67** | **0.71** |

#### Step 6: Model Export
- Best model serialized with `pickle.dump()` -> `diabetes_model.pkl`
- Fitted `StandardScaler` serialized -> `scaler.pkl`

---

### 8.2 Visualization Gallery

Charts embedded in the dashboard (`index.html`) using Chart.js:

#### Chart 1: Model Accuracy Comparison (Bar Chart)
- **Type:** Grouped bar chart
- **X-axis:** Model names (LR, RF, SVM, KNN, GBC)
- **Y-axis:** Accuracy (%)
- **Highlight:** Gradient Boosting bar is visually distinguished

#### Chart 2: Glucose Distribution by Outcome (Bar Chart)
- **Type:** Grouped bar chart
- **X-axis:** Glucose ranges (binned)
- **Y-axis:** Patient count
- **Grouping:** Diabetic vs Non-Diabetic overlay

---

## 9. Gallery

### Figure 9.1 — Login Page

[Login Page Interface Screenshot]

_The login interface features a centered glassmorphism card with PBKDF2-authenticated credential fields against a deep gradient background._

---

### Figure 9.2 — Dashboard Overview

[Dashboard Overview Screenshot]

_The main dashboard displays three summary metric cards: Total Records (768), Features Used (8), and Model Accuracy (78.5%), followed by the interactive chart section._

---

### Figure 9.3 — Model Accuracy Comparison Chart

[Model Comparison Chart Screenshot]

_A bar chart comparing the five tested classifiers. Gradient Boosting (78.5%) is the clear leader._

---

### Figure 9.4 — Glucose Distribution Chart

[Glucose Distribution Chart Screenshot]

_Distribution of glucose values split by diabetic vs. non-diabetic outcome, revealing higher glucose levels among diabetic patients._

---

### Figure 9.5 — Health Metrics Prediction Form

[Prediction Form Screenshot]

_The 8-field input form for entering patient health metrics. A random test case is pre-populated on page load._

---

### Figure 9.6 — Prediction Result Display

[Prediction Result Screenshot]

_The result card displaying "Diabetic" or "Not Diabetic" with color-coded visual indicator._

---

### Figure 9.7 — PDF Report Sample

[PDF Report Screenshot]

_A sample of the downloadable patient assessment PDF generated client-side using jsPDF._

---

## 10. Testing & Quality Assurance

### 10.1 Test Cases

| TC ID | Test Case Description | Input | Expected Result | Status |
|-------|----------------------|-------|-----------------|--------|
| **TC-01** | Valid login with correct credentials | `admin` / `pass` | Redirect to dashboard | Pass |
| **TC-02** | Invalid login — wrong password | `admin` / `wrong` | Error message on login page | Pass |
| **TC-03** | Invalid login — nonexistent user | `ghost` / `pass` | Error message on login page | Pass |
| **TC-04** | Diabetic prediction — high-risk inputs | Glucose=180, BMI=36, Age=55, DPF=0.9 | "Diabetic" | Pass |
| **TC-05** | Non-diabetic prediction — low-risk inputs | Glucose=89, BMI=22, Age=25, DPF=0.2 | "Not Diabetic" | Pass |
| **TC-06** | Missing model file graceful error | Delete `diabetes_model.pkl` | Error message displayed on dashboard | Pass |
| **TC-07** | Form submission with all zeros | All fields = 0 | Prediction returned (no crash) | Pass |
| **TC-08** | Random test case auto-fill | Page load (GET /dashboard) | Form pre-filled with valid values | Pass |
| **TC-09** | PDF report generation | Click "Download Report" | PDF file downloaded to browser | Pass |
| **TC-10** | SQL injection attempt in login | `username = ' OR 1=1 --` | Login fails (parameterized query blocks) | Pass |
| **TC-11** | Non-numeric input in prediction form | `glucose = "abc"` | Flask returns exception message | Pass |
| **TC-12** | Database not found | Delete `users.db` | Error logged; login gracefully fails | Pass |

---

### 10.2 Browser / Device Compatibility

| Browser | Version | OS | Login Page | Dashboard | Charts | PDF Export |
|---------|---------|----|------------|-----------|--------|------------|
| Google Chrome | 124+ | Windows 11 | Yes | Yes | Yes | Yes |
| Mozilla Firefox | 126+ | Windows 11 | Yes | Yes | Yes | Yes |
| Microsoft Edge | 124+ | Windows 11 | Yes | Yes | Yes | Yes |
| Safari | 17+ | macOS 14 | Yes | Yes | Yes | Yes |
| Chrome Mobile | 124+ | Android 13 | Yes | Yes | Yes | Limited |
| Safari Mobile | 17+ | iOS 17 | Yes | Yes | Yes | Limited |

> Note: PDF download on mobile browsers may vary by device due to file system access restrictions.

---

## 11. Maintenance & Future Scope

### Known Issues

| # | Issue | Severity | Notes |
|---|-------|----------|-------|
| **BUG-01** | Zero values in Glucose/Insulin fields are not validated as medically implausible on the frontend | Low | Should add range validation with warnings |
| **BUG-02** | Session state is not managed (no logout functionality) | Medium | Flask sessions or JWT tokens needed |
| **BUG-03** | Only a single pre-seeded admin user; no registration flow | Low | By design for demo, but limits multi-user use |
| **BUG-04** | Model accuracy (78.5%) may degrade on non-Pima populations due to demographic skew | High | Dataset is limited to Pima Indian women aged 21+ |
| **BUG-05** | Pickle deserialization carries a security risk if `.pkl` files are tampered | Medium | File integrity checks (checksums) recommended |

---

### Future Enhancements

| # | Enhancement | Priority | Estimated Effort |
|---|-------------|----------|-----------------|
| **FE-01** | Add user registration & multi-user support | High | Medium |
| **FE-02** | Implement Flask session management and a "Logout" route | High | Low |
| **FE-03** | Persist prediction history to the database for audit trails | Medium | Medium |
| **FE-04** | Add XGBoost or LightGBM models for improved accuracy | Medium | Medium |
| **FE-05** | Expose REST API endpoints (JSON responses) for third-party apps | Medium | Low |
| **FE-06** | Containerize the application with Docker | Low | Low |
| **FE-07** | Deploy to a cloud platform (Render / Railway / AWS EC2) | Medium | Medium |
| **FE-08** | Add SHAP explainability visualizations per prediction | High | High |
| **FE-09** | Implement real-time prediction via WebSockets | Low | High |
| **FE-10** | Expand the dataset to reduce Pima demographic bias | High | High |
| **FE-11** | Add CI/CD pipeline via GitHub Actions | Low | Medium |

---

## 12. Conclusion & References

### Conclusion

The **Diabetes Intelligence Platform** successfully demonstrates the complete lifecycle of a machine learning-driven web application — from raw data exploration and model selection through to a secure, interactive, and visually polished web deployment.

Key achievements include:
- **Model Performance:** Gradient Boosting classifier achieved **78.5% accuracy**, highest among five evaluated classifiers.
- **Security:** PBKDF2-SHA256 password hashing with 260,000 iterations and parameterized SQL queries protect the authentication layer.
- **User Experience:** Glassmorphism-inspired design, interactive Chart.js visualizations, and one-click PDF report generation.
- **Maintainability:** Clear separation of concerns — ML models decoupled from routes, database layer isolated, templates self-contained.

While the system is not intended for clinical use, it forms a solid foundation for production-grade enhancements and provides genuine educational value as a full-stack ML deployment reference.

---

### GitHub / Live Demo Links

| Resource | Link |
|----------|------|
| **GitHub Repository** | _(Add your GitHub repository URL here)_ |
| **Live Demo** | _(Add your deployed URL here)_ |
| **Sample PDF Report** | `reports/Diabetes prediction.pdf` |
| **Jupyter Notebook** | `notebooks/diabetes.ipynb` |

---

### Data Sources

| Source | Description | URL |
|--------|-------------|-----|
| Pima Indians Diabetes Dataset | Original dataset from NIDDK — 768 female patients of Pima Indian heritage | https://archive.ics.uci.edu/dataset/34/diabetes |
| Kaggle Mirror | Widely used Kaggle version of the dataset | https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database |
| scikit-learn Docs | GradientBoostingClassifier, StandardScaler documentation | https://scikit-learn.org |
| Flask Documentation | Web framework reference | https://flask.palletsprojects.com |
| Chart.js | JavaScript charting library | https://www.chartjs.org |
| jsPDF | Client-side PDF generation | https://github.com/parallax/jsPDF |

---

## 12.1 Project Limitations

| # | Limitation | Impact |
|---|------------|--------|
| **L-01** | Dataset limited to **female patients of Pima Indian heritage aged 21+**. Model may not generalize to other demographics. | High |
| **L-02** | Dataset contains only **768 samples**, constraining statistical robustness for deep learning approaches. | Medium |
| **L-03** | **Zero values** in clinical fields represent missing data. Median imputation may introduce bias. | Medium |
| **L-04** | **No real-time data pipeline** — the model cannot self-update from new patient data without manual retraining. | Medium |
| **L-05** | **Session management is absent** — unsuitable for multi-user concurrent production use. | High |
| **L-06** | Prediction is **binary (Diabetic / Not Diabetic)** with no confidence score output. | Medium |
| **L-07** | **Model explainability** (SHAP/LIME) not implemented — cannot explain why a prediction was made. | High |
| **L-08** | Flask **Werkzeug development server** is not suitable for high-concurrency production traffic. | Medium |
| **L-09** | **No HTTPS** configured — all traffic runs over HTTP, insecure outside `localhost`. | High |
| **L-10** | PDF generation uses **client-side jsPDF** with limited formatting capability. | Low |

---

## 12.2 Future Scope

### Short-Term (0-3 months)
1. **Flask session management & logout route** — Implement proper session handling using `flask.session`.
2. **Frontend input validation** — Add JavaScript range checks to flag medically implausible values.
3. **Confidence scores** — Use `model.predict_proba()` to return probability outputs alongside binary labels.
4. **Multi-user auth** — Add user registration endpoint and admin management dashboard.

### Medium-Term (3-9 months)
5. **Model improvement** — Train XGBoost or LightGBM models with hyperparameter tuning.
6. **SHAP explainability** — Integrate `shap` library to generate feature importance plots per prediction.
7. **Prediction history** — Log all predictions to SQLite with timestamps for audit and analytics.
8. **REST API** — Expose `/api/predict` returning JSON for third-party integrations.
9. **Docker containerization** — Package the app as a Docker image for reproducible deployment.

### Long-Term (9-24 months)
10. **Multi-disease model expansion** — Extend to predict other conditions using additional datasets.
11. **EHR integration** — Build FHIR-compliant connectors for electronic health record integration.
12. **MLOps pipeline** — Implement model versioning (MLflow), drift detection, and automated retraining.
13. **Mobile native app** — Develop iOS/Android companion app using React Native or Flutter.
14. **Federated Learning** — Train across decentralized institutions without centralizing patient data.

---

## 12.3 Results

### Final Model Performance Summary

| Metric | Value |
|--------|-------|
| **Algorithm** | Gradient Boosting Classifier |
| **Training Samples** | 614 (80% of 768) |
| **Test Samples** | 154 (20% of 768) |
| **Test Accuracy** | **78.5%** |
| **Precision (Class 1: Diabetic)** | 0.76 |
| **Recall (Class 1: Diabetic)** | 0.67 |
| **F1-Score (Class 1: Diabetic)** | 0.71 |
| **Dataset** | Pima Indians Diabetes Dataset |
| **Preprocessing** | Median imputation + StandardScaler |

### Model Comparison Results

| Rank | Model | Accuracy | F1-Score |
|------|-------|----------|----------|
| 1st | **Gradient Boosting** | **78.5%** | **0.71** |
| 2nd | Random Forest | 77.1% | 0.69 |
| 3rd | SVM | 76.2% | 0.67 |
| 4th | Logistic Regression | 75.3% | 0.66 |
| 5th | KNN | 73.8% | 0.64 |

### System Performance Results

| Metric | Result |
|--------|--------|
| Average prediction response time | < 200ms (local) |
| Login authentication time | < 300ms (PBKDF2 hashing) |
| PDF generation time | < 1 second (client-side) |
| Browser compatibility | Chrome, Firefox, Edge, Safari |
| Mobile responsiveness | Functional on 360px+ screens |

---

_End of Software Design Document_

---

**Document prepared for:** Diabetes Intelligence Platform | ML Project  
**Standard followed:** IEEE 1016 / Standard SDD Format  
**Version:** 1.0 | April 06, 2026
