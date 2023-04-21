"""from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC"""

import numpy as np
import pandas as pd
import random

soner = {"NO1" : 1.0, "NO2" : 2.0, "NO3" : 3.0, "NO4" : 4.0, "NO5" : 5.0}

def hent_priser(sone):
    with open(f"data/priser/{sone}.txt", "r") as file:
        return np.array(file.read().split("\n")).astype(float).tolist()
def hent_nedbor(sone):
    with open(f"data/nedbor/{sone}.txt", "r") as file:
        return np.array(file.read().split("\n")).astype(float).tolist()
def hent_temps(sone):
    with open(f"data/temperatur/{sone}.txt", "r") as file:
        return np.array(file.read().split("\n")).astype(float).tolist()

def create_model():
    priser = []
    nedbor = []
    temps = []
    soneer = []

    for sone in soner:
        prise = hent_priser(sone)
        nedbo = hent_nedbor(sone)
        tempse = hent_temps(sone)

        for i in range(len(prise)):
            priser.append(prise[i])
            nedbor.append(nedbo[i])
            temps.append(tempse[i])
            soneer.append(soner[sone])

    indices = random.sample(range(len(priser)), len(priser))

    priser = [priser[i] for i in indices]
    nedbor = [nedbor[i] for i in indices]
    temps = [temps[i] for i in indices]
    soneer = [soneer[i] for i in indices]

    dataframe = pd.DataFrame()
    
    dataframe["nedbor"] = nedbor
    dataframe["temps"] = temps
    dataframe["soner"] = soneer
    dataframe["priser"] = priser

    dataframe.to_csv("dataset.csv", index=False)

    """

    train_priser = priser[0:2300]; test_priser = priser[2300:-1]
    train_nedbor = nedbor[0:2300]; test_nedbor = nedbor[2300:-1]
    train_temps = temps[0:2300]; test_temps = nedbor[2300:-1]
    train_soner = soneer[0:2300]; test_soner = soneer[2300:-1]

    
    X = np.column_stack((train_nedbor, train_temps, train_soner))
    Y = np.array(train_priser)

    model = RandomForestRegressor()
    model.fit(X, Y) 

    sum_error = 0
    print("TESTING:")
    for i in range(0, len(test_priser)):
        predicted = model.predict(np.array([[test_nedbor[i], test_temps[i], test_soner[i]]]))[0]
        print(f"Expected: {test_priser[i]}, predicted: {predicted}")

        sum_error += abs(test_priser[i] - predicted) / test_priser[i]
    
    sum_error_average = sum_error/len(test_priser)
    print(sum_error_average)
    """
    

def hovedprogram():
    create_model()

hovedprogram()