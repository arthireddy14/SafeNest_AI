# 🏠 SafeNest AR

## Secure Homes. Peaceful Journeys.

SafeNest AR is an AI-powered home security and vacation monitoring platform designed to help families protect their homes while they are away. The system analyzes security events, predicts potential threats using Machine Learning, generates intelligent safety recommendations, and visualizes threats through an Augmented Reality-inspired Security Map.

---

## 📌 Problem Statement

Families often worry about the safety of their homes while traveling for vacations, business trips, festivals, or emergencies.

Traditional security systems generate alerts but often fail to provide intelligent threat assessment, centralized monitoring, and visual situational awareness.

---

## 💡 Solution

SafeNest AR combines Artificial Intelligence and Augmented Reality concepts to:

* Monitor home security events
* Predict threat levels using Machine Learning
* Assess security risks in real-time
* Generate safety recommendations
* Visualize threats through an AR-inspired security map
* Provide centralized family safety management

---

## 🚀 Key Features

### 👨‍👩‍👧 Family Registry

Manage and register authorized family members.

### ✈ Vacation Mode

Enable enhanced security monitoring when homeowners are away.

### 🤖 AI Threat Prediction

Predicts threat levels using a Random Forest Machine Learning model.

### 📊 Risk Assessment

Generates risk scores based on detected activities and security events.

### 🛡 Safety Recommendations

Provides intelligent recommendations based on threat severity.

### 🚨 Emergency Alerts

Displays security incidents and alert notifications.

### 📱 AR Security Map

Visualizes threat zones across different areas of the home.

### 📜 Security Timeline

Tracks and displays recent security events and activities.

---

## 🏗 System Architecture

Family Registry
↓
Vacation Mode
↓
Threat Analysis
↓
AI Threat Prediction Model
↓
Risk Assessment
↓
Safety Recommendations
↓
Emergency Alerts
↓
AR Security Visualization

---

## 🖼 Project Screenshots

### 🏠 Home Dashboard

![Dashboard](images/safenest_dashboard.png)

---

### 👨‍👩‍👧 Family Registry

![Family Registry](images/family_registry_image.png)

---

### ✈ Vacation Mode

![Vacation Mode](images/vacation_mode.png)

---

### 🚨 Threat Analyzer

![Threat Analyzer](images/threat_analyzer_image.png)


---

### 🚨 Emergency Alerts

![Emergency Alerts](images/emergency_alerts.png)

---

### 📱 AR Security Map

![AR Security Map](images/ar_security_map.png)

---

### 📜 Security Timeline

![Security Timeline](images/security_timeline.png)

---

## 🤖 Machine Learning Model

### Algorithm Used

* Random Forest Classifier

### Input Features

* Person Type
* Time of Day
* Motion Detection
* Door Activity
* Window Activity
* Vacation Mode Status
* Previous Security Incidents

### Output

* Low Threat
* Medium Threat
* High Threat

### Model Performance

* Accuracy: 99.5%

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning

* Scikit-learn
* Random Forest Classifier

### Data Handling

* Pandas
* NumPy

### Storage

* JSON

### Version Control

* Git & GitHub

---

## 📂 Project Structure

SafeNest_AR/

├── app.py

├── pages/

│   ├── family_registry.py

│   ├── vacation_mode.py

│   ├── threat_analyzer.py

│   ├── emergency_alerts.py

│   ├── ar_visualization.py

│   └── security_timeline.py

├── data/

│   ├── family.json

│   ├── vacation_mode.json

│   └── stats.json

├── images/

│   ├── safenest_dashboard.png

│   ├── family_registry_image.png

│   ├── vacation_mode.png

│   ├── threat_analyzer_image.png

│   ├── emergency_alerts.png

│   ├── security_timeline.png

│   └── safenest_homepage.png

├── threat_model.pkl

├── train_model.py

├── generate_dataset.py

└── README.md

---
## Vision

SafeNest AR

AI-Powered Security Monitoring & Threat Visualization Platform

Use Cases:

🏠 Homes

🏦 Banks

🏪 Shops

🏢 Offices

🏫 Schools

🏬 Warehouses
---

## 🔮 Future Scope

* Real-time AR Camera Overlay
* Face Recognition for Visitor Identification
* Smart CCTV Integration
* IoT Door and Window Sensors
* Mobile Push Notifications
* Voice-based Emergency Assistant
* Security Guard Monitoring
* ATM and Bank Security Monitoring
* Smart City Safety Integration

---

## 🎯 Hackathon Theme Alignment

SafeNest AR aligns with the Open Innovation and Augmented Reality themes by combining:

* Artificial Intelligence
* Security Analytics
* Risk Prediction
* AR-inspired Threat Visualization
* Smart Home Monitoring

to create a next-generation family safety platform.

---

## ▶ How to Run

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Application

```bash
streamlit run app.py
```

---

## 👩‍💻 Developed By

C.Arthi Reddy
K.Rishitha Srija


