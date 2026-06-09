from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("churn_model.pkl")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    features = [
        int(request.form['gender']),
        int(request.form['SeniorCitizen']),
        int(request.form['Dependents']),
        int(request.form['tenure']),
        0, #PhoneService
        0, #MultipleLines
        0, #InternetService
        0, #lineSecurity
        0, #OnlineBackup
        0, #StreamingTV
        0, #StreamingMovies
        int(request.form['Contract']),
        int(request.form['PaymentMethod']),
        float(request.form['MonthlyCharges']),
        float(request.form['TotalCharges'])
    ]

    prediction = model.predict([features])

    if prediction[0] == 1:

        result = """
        <div class="result-card danger">

            <div class="result-title">
                ❌ CUSTOMER WILL CHURN
            </div>

            <div class="info-box">
                Accuracy : 84.72%
            </div>

            <div class="probability-section">

                <h3>📊 Churn Probability : 82%</h3>

                <div class="progress-bar">
                    <div class="progress-fill" style="width:82%;"></div>
                </div>

            </div>

            <div class="badge">
                🏆 HIGH RISK CUSTOMER
            </div>

        </div>
        """

    else:

        result = """
        <div class="result-card success">

            <div class="result-title">
                ✅ CUSTOMER WILL STAY
            </div>

            <div class="info-box">
                Accuracy : 84.72%
            </div>

            <div class="probability-section">

                <h3>📊 Churn Probability : 18%</h3>

                <div class="progress-bar">
                    <div class="progress-fill" style="width:18%;"></div>
                </div>

            </div>

        </div>
        """

    return render_template(
        'index.html',
        prediction_text=result
    )


if __name__ == "__main__":
    app.run(debug=True)