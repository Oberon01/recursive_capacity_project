import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def train_model(data_path):
    df = pd.read_csv(data_path)
    
    X = df.drop(columns=["recursive_capacity"])
    y = df["recursive_capacity"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("Mean Squared Error:", mse)
    print("R-squared:", r2)

    return model
