"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.9
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report

def train_model(X_train, y_train,params:dict):
    model = LogisticRegression(penalty=params["penality"],class_weight=params["class_weight"])
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print("Accuracy Of Model is: ",accuracy)
    print(report)
    return accuracy, report