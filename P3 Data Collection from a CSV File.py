import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'P3_people_data.csv')

print("First five rows of the dataset")
print(data.head())

print("\n Summary statistics of numerical column: ")
print(data.describe())

print("\nData information")
print(data.info())

plt.figure(figsize=(8,6))
sns.histplot(data['Age'], bins=10, kde=True)
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(data=data, x='Gender', y='Age')
plt.title("Boxplot of Age by Gender")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.show()






"""
P3_people_data.csv
Name,Age,Gender,Salary,Education
Alice,30,Female,50000,Master's
Bob,25,Male,60000,Bachelor's
Charlie,35,Male,75000,Ph.D.
David,28,Male,45000,Bachelor's
Eve,32,Female,55000,Master's
Frank,22,Male,42000,Bachelor's
Grace,29,Female,70000,Ph.D.
Hannah,27,Female,52000,Bachelor's
Isaac,40,Male,80000,Master's
"""

