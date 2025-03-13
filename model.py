import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_and_predict(df):
    if df.empty:
        return "No data available."

    df["date"] = pd.to_datetime(df["date"])
    df["timestamp"] = df["date"].map(pd.Timestamp.timestamp)

    X = df[["timestamp"]]
    y = df["usage"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    future_dates = pd.date_range(start=df["date"].max(), periods=10, freq="D")
    future_timestamps = future_dates.map(pd.Timestamp.timestamp).values.reshape(-1, 1)
    predictions = model.predict(future_timestamps)

    return list(zip(future_dates.strftime("%Y-%m-%d"), predictions))
