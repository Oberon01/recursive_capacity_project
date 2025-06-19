from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
df = pd.read_csv("data/trait_data.csv")

# Define features and target
X = df.drop(columns=["recursive_capacity"])
y = df["recursive_capacity"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
coefficients = dict(zip(X.columns, model.coef_))
intercept = model.intercept_

mse, r2, coefficients, intercept
print(mse)
print(r2)
print(coefficients)
print(intercept)