# Step 1: Import required libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Load the Iris dataset
iris = load_iris()
X = iris.data      # Input features
y = iris.target   # Target class labels

# Step 3: Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Step 4: Create Decision Tree Classifier model
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Step 5: Predict the test data
y_pred = classifier.predict(X_test)

# Step 6: Evaluate the model
print("Accuracy of the model:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
