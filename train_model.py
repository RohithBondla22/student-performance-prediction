import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib


# 1. Load the dataset
data = pd.read_csv("data/students.csv")

# 2. Select input features
X = data[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "assignments_completed"
    ]
]

# 3. Select the value we want to predict
y = data["final_score"]

# 4. Split data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 5. Create the machine learning model
model = LinearRegression()

# 6. Train the model
model.fit(X_train, y_train)

# 7. Make predictions using test data
predictions = model.predict(X_test)

# 8. Evaluate the model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model Training Complete!")
print("-------------------------")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

# 9. Save the trained model
joblib.dump(model, "model/student_model.pkl")

print("-------------------------")
print("Model saved successfully!")
print("Location: model/student_model.pkl")