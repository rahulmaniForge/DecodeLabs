print("\n===== STUDENT PERFORMANCE CLASSIFICATION USING AI =====\n")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("student_data.csv")

print("Dataset:")
print(data)

# Features and Target
X = data[['Hours','Attendance','Assignments']]
y = data['Result']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Models
dt_model = DecisionTreeClassifier()
knn_model = KNeighborsClassifier(n_neighbors=3)

# Train Models
dt_model.fit(X_train, y_train)
knn_model.fit(X_train, y_train)

print("\nTesting Model...")

# KNN Predictions
predictions = knn_model.predict(X_test)

print("\n===== MODEL TEST RESULTS =====")

results = pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': predictions
})

print(results)

# Accuracy
knn_accuracy = accuracy_score(y_test, predictions)
dt_accuracy = dt_model.score(X_test, y_test)

print("\n===== ALGORITHM COMPARISON =====")
print(f"Decision Tree Accuracy: {dt_accuracy*100:.2f}%")
print(f"KNN Accuracy: {knn_accuracy*100:.2f}%")

# Interactive Prediction
print("\n===== NEW STUDENT PREDICTION =====")

hours = int(input("Enter Study Hours: "))
attendance = int(input("Enter Attendance %: "))
assignments = int(input("Enter Assignments Completed: "))

new_student = pd.DataFrame({
    'Hours':[hours],
    'Attendance':[attendance],
    'Assignments':[assignments]
})

result = knn_model.predict(new_student)

print("\nPrediction:", result[0])
