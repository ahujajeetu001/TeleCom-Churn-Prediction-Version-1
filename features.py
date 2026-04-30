import pandas as pd

#Loading the Data
df = pd.read_csv("data/cleaned_data.csv")
print("Before Ecoding:",df.shape)


#Converting In Numberic
df = pd.get_dummies(df,drop_first=True)
print("After Encoding:",df.shape)

#Saving
df.to_csv("data/final_data.csv",index=False)
print("Saved")