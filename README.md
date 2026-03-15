# Cyberbullying_detection_tool
Cyberbullying Detection System using Machine Learning and Flask. This project analyzes text messages and predicts whether they contain cyberbullying content using a Logistic Regression model and TF-IDF vectorization, with a user-friendly web interface built using Flask.


# Cyberbullying Detection System

## Overview
The Cyberbullying Detection System is a machine learning-based web application designed to identify harmful or abusive text messages that may contain cyberbullying content. The system helps promote safer online communication by automatically detecting offensive language in user-provided text.

## Features
- Detects cyberbullying in text messages
- Real-time prediction through a web interface
- Text preprocessing and feature extraction using TF-IDF
- Machine learning model for classification
- Simple and interactive web application using Flask

## Technologies Used
- Python
- Machine Learning (Logistic Regression)
- Natural Language Processing (TF-IDF Vectorization)
- Flask (Web Framework)
- HTML, CSS, JavaScript
- Scikit-learn
- Pickle (for saving trained model)

## How It Works
1. User enters a message in the web interface.
2. The text is cleaned and preprocessed.
3. TF-IDF converts the text into numerical features.
4. The trained Logistic Regression model predicts whether the message contains cyberbullying.
5. The result is displayed on the webpage.

## Project Structure
Cyberbullying_Flask
│
├── app.py
├── cyberbullying_model.pkl
├── tfidf.pkl
├── templates
│ └── index.html
└── README.md

## Installation
1. Clone the repository
2. Create a virtual environment
3. Install required packages

pip install flask
pip install scikit-learn
pip install numpy
pip install pandas

4. Run the application
python app.py

5. Open in browser

## Applications
- Social media monitoring
- Online community moderation
- Educational platforms
- Chat filtering systems

## Future Improvements
- Add deep learning models for higher accuracy
- Support multiple languages
- Detect different types of bullying
- Deploy the application online

