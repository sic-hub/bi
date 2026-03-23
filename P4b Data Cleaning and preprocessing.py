import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Load dataset
file_path = r"P4b_sample_data.csv"
data = pd.read_csv(file_path, encoding="ISO-8859-1")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# Select numerical columns
numerical_columns = ['Temperature', 'Humidity']

# Summary statistics before cleaning
print("\nSummary statistics before cleaning:")
print(data[numerical_columns].describe())

# Check missing values
missing_values = data[numerical_columns].isnull().sum()
print("\nMissing values before cleaning:")
print(missing_values)

# Handle missing values
data['Temperature'].fillna(data['Temperature'].mean(), inplace=True)

# Convert categorical columns to numerical
data['Outlook'] = data['Outlook'].astype('category').cat.codes
data['Wind'] = data['Wind'].map({'Weak': 0, 'Strong': 1})
data['Play'] = data['Play'].map({'No': 0, 'Yes': 1})

# Save cleaned dataset
cleaned_file_path = r"P4b_sample_data.csv"
data.to_csv(cleaned_file_path, index=False)

# Display cleaned data
print("\nAfter cleaning:")
print(data.head())

# Updated numerical columns
numerical_columns = ['Outlook', 'Temperature', 'Humidity', 'Wind', 'Play']

# Summary statistics after cleaning
print("\nSummary statistics after cleaning:")
print(data[numerical_columns].describe())

# Check missing values after cleaning
missing_values = data[numerical_columns].isnull().sum()
print("\nMissing values after cleaning:")
print(missing_values)




"""
Outlook,Temperature,Humidity,Wind,Play
2,85,85.0,,
2,80,90.0,,
0,83,78.0,,
1,70,96.0,,
1,68,80.0,,
1,65,,,
0,64,65.0,,
2,72,95.0,,
2,69,70.0,,
1,75,80.0,,
2,75,70.0,,
0,72,90.0,,
0,81,75.0,,
1,71,80.0,,
"""
