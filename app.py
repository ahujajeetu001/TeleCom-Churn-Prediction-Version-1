from flask import Flask,render_template,request
import pandas as pd
import pickle

#Starting Flask App
app=Flask(__name__)

#Model Loading in read binary
model=pickle.load(open("model.pkl","rb"))

#Home Route
@app.route("/")
def home():
    return render_template("index.html")

#Submit with User Values
@app.route("/predict",methods=["POST"])
def predict():
    tenure=int(request.form["tenure"])
    monthly=float(request.form["monthly"])
    total=float(request.form["total"])
    gender=(request.form["gender"])
    contract=(request.form["contract"])
    internet=(request.form["internet"])
    #Data frame
    data=pd.DataFrame({"tenure":[tenure],
                    "MonthyCharges":[monthly],
                    "TotalCharges":[total],
                    "gender":[gender],
                    "Contract":[contract],
                    "InternetService":[internet]
                    }) 
    data =pd.get_dummies(data)
    #Reordering as Per Model
    data=data.reindex(columns=model.feature_names_in_,fill_value=0)
    print(model.feature_names_in_)
    print(type(model))

    #Predictions
    prediction=model.predict(data)[0]
    result="Customer Will Churn" if prediction==1 else "Customer Will Stay"
    return render_template("index.html",prediction=result)




if __name__=="__main__":
    port=int(os.version.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)
