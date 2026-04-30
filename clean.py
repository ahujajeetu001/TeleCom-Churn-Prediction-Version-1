import pandas as pd

#Loading the Data
df = pd.read_csv("data/data.csv")
print("Shape Before Cleaning:",df.shape)

#Cleaning unwanted Columns
if "customerID" in df.columns:
    df.drop("customerID",axis=1,inplace=True)
#inplace is used to edit in Original DataFrame itself


#Charges are in string converting to Float
df["TotalCharges"]=pd.to_numeric(df["TotalCharges"],errors="coerce")
# we have used coerce if values is not Available it will be set as NAN
# but we have raise as well which will raise an exception 


#Removing Missing Values and saving in same DataFrame
df.dropna(inplace=True)

#Mapping 0 & 1
df["Churn"]=df["Churn"].map({"Yes":1, "No":0})
print("Current Shape :",df.shape)

#Saved Cleaned Data
df.to_csv("data/cleaned_data.csv",index=False)
print("Saved")
