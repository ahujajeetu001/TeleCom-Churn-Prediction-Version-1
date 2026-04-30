import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Loading the Data
df = pd.read_csv("data/data.csv")

#Info In Data
print("Shape: ", df.shape)
print("\nInfo:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

# Target Column
print("\n Churn Count:")
print(df['Churn'].value_counts())


#Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

#Stats
#print("\nStats:")
#print(df.describe())

#Plotting
#Churn Count
#sns.countplot(x='Churn',data=df)
#plt.title("Churn Count")
#plt.show()

#Monthly Charges vs Churn
#sns.boxplot(x="Churn",y="MonthlyCharges",data=df)
#plt.title("Monthly Charges VS Churn")
#plt.show()

#Tenure VS Churn
#sns.boxplot(x="Churn",y="tenure",data=df)
#plt.title("Tenure VS Churn")
#plt.show()

#Contract VS Churn
#sns.countplot(x="Contract",hue="Churn",data=df)
#plt.title("Contract VS Churn")
#plt.show()

