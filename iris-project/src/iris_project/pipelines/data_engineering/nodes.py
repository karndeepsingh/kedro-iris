"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.9
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report



def preprocessing(iris):
    features = iris.columns[:-1]
    target = iris.columns[-1]
    X = iris[features]
    y = iris[target]
    # Standardize the features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    return X, y

def split_data(X, y, params:dict):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=params["test_size"], random_state=params["random_state"])
    return X_train, X_test, y_train, y_test