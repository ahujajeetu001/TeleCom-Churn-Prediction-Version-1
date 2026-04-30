import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#Loading Final Data
df=pd.read_csv("data/final_data.csv")

print("Shape:", df.shape)

x=df.drop("Churn",axis =1)
y=df["Churn"]

#Training
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=42)
print("Training Size:", x_train.shape)
print("Testing Size:", x_test.shape)

# Model Fitting
model = RandomForestClassifier(max_depth=10,n_estimators=100,random_state=42)
model.fit(x_train,y_train)
print("Trained!")

#Accuracy
train_pred=model.predict(x_train)
test_pred=model.predict(x_test)
print("Training Accuracy ",accuracy_score(y_train,train_pred))
print("Testing Accuracy ",accuracy_score(y_test,test_pred))


#Generating PKL in writebinary(wb)
with open("model.pkl","wb")as f:
    pickle.dump(model,f)
print("Pickle File Genrated!")