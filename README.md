
---

# 🏡 Immo-Eliza Deployment — Streamlit App

This repository contains the deployment of a machine learning model that predicts real-estate prices for Belgian properties.
The project was developed as part of the **Immo-Eliza Deployment** assignment and focuses on providing a simple, user-friendly web interface built with **Streamlit**.

---

## 🚀 Project Overview

The goal of this project was to make the trained prediction model accessible to non-technical users through a lightweight web application.

In this implementation, I chose to deliver:

✅ A fully functional **Streamlit application**



The app loads the model and preprocessing pipeline, takes the user’s input, and returns a property price estimate.

---

## 📂 Repository Structure

```
IMMO-ELIZA-DEPLOYMENT/
│
├── models/                # Saved preprocessing pipelines + trained model
│
├── app.py                 # Streamlit application
├── predict.py             # Model loading + preprocessing + prediction
│
├── background_dark.jpg    # App assets
├── background_light.jpg
│
├── requirements.txt       # Dependencies
├── pyproject.toml
├── .gitignore
└── README.md
```

---

## 🧠 How It Works

### 1. **Model & Preprocessing**

The `predict.py` module:

* Loads the saved model artifacts
* Preprocesses incoming data to match training format
* Returns a final predicted price

### 2. **Streamlit Interface (`app.py`)**

The Streamlit app:

* Displays a clean UI for users to enter property features
* Sends the inputs to the preprocessing + model pipeline
* Shows the predicted price instantly

---

## ▶️ Running the App Locally

### **1. Clone the repository**

```bash
git clone https://github.com/<your-username>/immo-eliza-deployment.git
cd immo-eliza-deployment
```

### **2. Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate      # On Linux/Mac
.venv\Scripts\activate         # On Windows
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run Streamlit**

```bash
streamlit run app.py
```

The app will open automatically in your browser at:

```
http://localhost:8501/
```

---

## 🛠️ Tools Used

* **Python 3**
* **Streamlit** — web UI
* **Scikit-learn** — model + preprocessing
* **Pandas / NumPy** — data handling

---

## 🌐 Deployment

This project was deployed using **Streamlit Community Cloud**.

🔗 **Live App:** 
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://immoeliza-price-predictor.streamlit.app/)


---

## 📌 Future Improvements

If expanding later, possible additions include:

* Adding a **FastAPI backend**
* Add a FastAPI backend with Docker support for deployment on Render.
* Enabling batch predictions
* Adding more visualizations or explainability features (e.g., SHAP)

---

## 🙌 Acknowledgments

This project was created during the AI Bootcamp at __BeCode.org.__ <br>
Feel free to reach out or connect with me on [LinkedIn](https://www.linkedin.com/in/brigi-bodi/)!

---