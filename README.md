🏏 IPL Prediction System (First Inning Score Prediction/Match Win Prediction)
Machine Learning + Streamlit Web App
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python"> <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit"> <img src="https://img.shields.io/badge/Machine%20Learning-Model-green?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"> </p>
📌 Overview

This project is a Machine Learning-powered IPL prediction web application built using Streamlit.

It provides:

📊 First Innings Score Prediction
🏆 Match Winner Prediction

The models are trained on historical IPL data and exposed through a clean multi-page UI.

🌐 Live Demo

👉 (Add your deployed link here)

https://your-app-name.streamlit.app
🎬 App Preview (GIF)

📌 Replace this with your screen recording GIF

![App Demo](assets/demo.gif)
🖼️ Screenshots
🏠 Home Page
![Home](assets/home.png)
📊 Score Predictor
![Score Predictor](assets/score.png)
🏆 Match Predictor
![Match Predictor](assets/match.png)
🚀 Features
🔹 First Innings Score Prediction

Predicts final score using:

Batting & Bowling Teams
Current Score
Overs Completed
Wickets Fallen
Last 5 overs performance
🔹 Match Winner Prediction

Predicts winner based on:

Teams
Toss Winner
Toss Decision
Venue
Season
🔹 Multi-Page Streamlit App
🏠 Home Page
📊 Score Predictor
🏆 Match Predictor
🧠 Machine Learning Models
Task	Model
Score Prediction	XGBoost Regressor
Match Prediction	Random Forest Classifier
📊 Dataset
IPL data from 2008 – 2018
Includes 8 major teams
❌ Excludes newer teams like:
Gujarat Titans (GT)
Lucknow Super Giants (LSG)
⚠️ Limitations
Model trained on older data (2008–2018)
May not reflect current IPL trends
Predictions are approximate
🗂️ Project Structure
IPL-Prediction/
│
├── main.py          # Navigation (Entry point)
├── home.py          # Welcome Page
├── app.py           # Score Predictor
├── app1.py          # Match Predictor
│
├── model.pkl        # Match prediction model
├── pipe.pkl         # Score prediction pipeline
├── img.jpg
│
├── assets/          # Screenshots & GIFs
│   ├── demo.gif
│   ├── home.png
│   ├── score.png
│   └── match.png
│
├── requirements.txt
└── README.md
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/ipl-prediction.git
cd ipl-prediction
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the App
streamlit run main.py
📦 Requirements
streamlit
pandas
numpy
scikit-learn==1.4.1.post1
xgboost
joblib
pillow
🎯 Future Enhancements
📈 Win probability visualization
🔄 Real-time match prediction
🤖 Deep learning models
📊 Player-level analytics