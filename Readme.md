# Spam Shield – AI Spam Detector 

## Project Overview

Spam Shield is an AI-powered spam detection web application that classifies SMS messages as **Spam** or **Not Spam** using Machine Learning. The application uses TF-IDF vectorization and a Multinomial Naive Bayes model to analyze message content and provide real-time predictions.

---

## Features

- Real-time Spam Detection
- Machine Learning-based Classification
- FastAPI REST API Backend
- Responsive Frontend Interface
- Spam Confidence Score
- Easy-to-use User Interface
- Real-world SMS Dataset Training

---

## Tech Stack

### Backend
- Python
- FastAPI
- Scikit-learn
- Pandas
- Joblib

### Frontend
- HTML
- CSS
- JavaScript

### Machine Learning
- TF-IDF Vectorizer
- Multinomial Naive Bayes

---

## Project Workflow

User Message
↓
Frontend Interface
↓
FastAPI Backend
↓
TF-IDF Vectorization
↓
Naive Bayes Model
↓
Prediction Result
↓
Frontend Display

---

## How It Works

1. User enters a message.
2. Frontend sends the message to the FastAPI backend.
3. Backend converts text into numerical vectors using TF-IDF.
4. The trained Naive Bayes model analyzes the message.
5. Prediction is generated as Spam or Not Spam.
6. Result is displayed to the user along with confidence score.

---

## Example

### Input

Win a free iPhone now! Click here to claim your prize.

### Output

Prediction: Spam

Confidence: 96%

---

## Project Structure

spam-detector/

├── backend/

│   ├── main.py

│   ├── train_model.py

│   ├── model.pkl

│   ├── vectorizer.pkl

│   └── requirements.txt

│

├── frontend/

│   ├── index.html

│   ├── style.css

│   └── script.js

│

├── README.md

└── .gitignore

---

## Future Enhancements

- Prediction History Storage
- PostgreSQL Database Integration
- Multiple Model Comparison
- Email Spam Detection
- User Authentication
- Cloud Deployment
- Multilingual Support

---

## Skills Demonstrated

- Machine Learning
- Text Classification
- Data Preprocessing
- FastAPI Development
- REST API Development
- Frontend-Backend Integration
- Git & GitHub

---

## Author

Madhura Bansod
