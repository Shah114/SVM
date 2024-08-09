# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Universal Bank Data
df = pd.read_csv('UniversalBank.csv') # copy the path of dataset
df.head()

# Checking for null values
sum_n = df.isnull().sum()
print(f"Sum of null values: {sum_n}")

# Dropping ID and ZIP Code columns from the dataset
df1 = df.drop(["ID", "ZIP Code"], axis=1)
df1.head()

"""Heatmap"""
plt.figure(figsize=(15,8))
plt.title("Heatmap showing Correlation between all the features", fontsize=20)
sns.heatmap(df1.corr(),annot = True, cmap='mako')
plt.show()

zero_class = df1[df1.CreditCard==0]
print(f"Shape of zero class: {zero_class.shape}")

one_class = df1[df1.CreditCard==1]
print(f"Shape of one class: {one_class.shape}")

"""Scatter Plot"""
# Income vs Experience scatter plot
plt.xlabel('Income')
plt.ylabel('Experience')
plt.scatter(zero_class['Income'],zero_class['Experience'], color = 'green', marker='+')
plt.scatter(one_class['Income'], one_class['Experience'], color = 'red', marker='.')
plt.show()

# CCAvg vs Family scatter plot
plt.xlabel('CCAvg')
plt.ylabel('Family')
plt.scatter(zero_class['CCAvg'],zero_class['Family'], color = 'blue', marker='+')
plt.scatter(one_class['CCAvg'], one_class['Family'], color = 'red', marker='.')
plt.show()

"""Scaling the Data"""
# Scaling the data using Standard Scaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled = scaler.fit(df1.drop('CreditCard', axis=1)).transform(df1.drop('CreditCard', axis=1))
df_scaled = pd.DataFrame(scaled, columns=df1.columns[:-1])
head_of_scaled = df_scaled.head()
print(f"Head of scaled data: {head_of_scaled}")

# Splitting the columns in to dependent variable (x) and independent variable (y).
x = df_scaled
y = df1['CreditCard']

"""Implementation of SVM"""
# Split data in to train and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Apply SVM Model
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
svc = SVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
print("Model accuracy: {0:0.3f}".format(accuracy_score(y_test, y_pred)))

# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm_matrix = pd.DataFrame(data=cm, columns=['Actual Positive:1', 'Actual Negative:0'],
                                index=['Predict Positive:1', 'Predict Negative:0'])

sns.heatmap(cm_matrix, annot=True, fmt='d', cmap='mako')
plt.show()

# Classification Report
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))