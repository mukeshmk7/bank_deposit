from flask import Flask, render_template, request, redirect
from joblib import load
import warnings
warnings.filterwarnings('ignore')

model = load('model.pkl')
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form.get("age"))
    balance = float(request.form.get("balance"))
    duration = float(request.form.get("duration"))
    campaign = int(request.form.get("campaign"))
    previous = int(request.form.get("previous"))
    marital = int(request.form.get("marital"))
    default = int(request.form.get("default"))
    housing = int(request.form.get("housing"))
    loan = int(request.form.get("loan"))
    contact_others = int(request.form.get("contact_others"))
    contact_telephone = int(request.form.get("contact_telephone"))
    poutcome_other = int(request.form.get("poutcome_other"))
    poutcome_success = int(request.form.get("poutcome_success"))
    output = model.predict([[age, balance, duration, campaign, previous, marital, default,
                                  housing, loan, contact_others, contact_telephone, poutcome_other, poutcome_success]])
    if output == 0:
        return render_template('predict.html', output="Customer will not deposit")
    else:
        return render_template('predict.html', output="Customer will deposit")

if __name__ == '__main__':
    app.run()