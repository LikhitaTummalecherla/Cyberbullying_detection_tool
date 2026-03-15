from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# =============================
# 1. Load Trained Model
# =============================

model = pickle.load(open("cyberbullying_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

# =============================
# 2. Text Cleaning Function
# =============================

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# =============================
# 3. Home Route
# =============================

@app.route("/")
def home():
    return render_template("index.html")

# =============================
# 4. Predict Route
# =============================

@app.route("/predict", methods=["POST"])
def predict():

    msg = request.form['message']

    clean = clean_text(msg)
    vec = tfidf.transform([clean])

    result = model.predict(vec)[0]

    if result == 1:
        output = "Cyberbullying Detected"
    else:
        output = "Normal Message"

    return render_template("index.html",
                           prediction=output,
                           text=msg)

# =============================
# 5. Run
# =============================

if __name__ == "__main__":
    app.run(debug=True)
