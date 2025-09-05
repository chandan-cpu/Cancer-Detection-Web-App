from flask import Flask,render_template,request,url_for
import pickle
import pandas as pd
import numpy as npcls
import joblib
model = pickle.load(open('pipe.pkl','rb'))
model_1 = joblib.load(open('breast_cancer.joblib','rb'))

app =  Flask(__name__)

@app.route("/")

def main():
    return render_template("home.html")

@app.route("/forms")
def forms():
    return render_template("Helthform.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/Service")
def Service():0.
    return render_template("service.html")

@app.route("/Contact")
def Contact():
    return render_template("Contact.html")
@app.route("/About")
def About():
    return render_template('about.html')

@app.route('/predict',methods=['POST'])
def predict():
    GENDER = request.form['GENDER']
    AGE = request.form['AGE']
    SMOKING=request.form['SMOKING']
    YELLOW_FINGERS= request.form['YELLOW_FINGERS']
    ANXIETY	= request.form['ANXIETY']
    PEER_PRESSURE = request.form['PEER_PRESSURE']
    CHRONIC_DISEASE = request.form['CHRONIC_DISEASE']

    FATIGUE	= request.form['FATIGUE']
    ALLERGY = request.form['ALLERGY']
    WHEEZING = request.form['WHEEZING']
    ALCOHOL_CONSUMING = request.form['ALCOHOL_CONSUMING']
    COUGHING = request.form['COUGHING']
    SHORTNESS_OF_BREATH	 = request.form['SHORTNESS_OF_BREATH']
    SWALLOWING_DIFFICULTY = request.form['SWALLOWING_DIFFICULTY']
    CHEST_PAIN = request.form['CHEST_PAIN']
    input_2=pd.DataFrame([[GENDER,AGE,SMOKING,YELLOW_FINGERS,
                           ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,
                           FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]],columns=['GENDER','AGE','SMOKING',
                                                                 'YELLOW_FINGERS','ANXIETY','PEER_PRESSURE','CHRONIC DISEASE'
                                                                 ,'FATIGUE','ALLERGY','WHEEZING','ALCOHOL CONSUMING','COUGHING'
                                                                 ,'SHORTNESS OF BREATH','SWALLOWING DIFFICULTY','CHEST PAIN'])

    pred= model.predict(input_2)

    return render_template('result.html',value=pred)


if __name__== "__main__":
    app.run(debug=True)