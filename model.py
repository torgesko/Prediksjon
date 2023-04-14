from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn2pmml import PMMLPipeline, sklearn2pmml
import numpy as np
import random

def hent_priser(sone):
    with open(f"data/priser/{sone}.txt", "r") as file:
        priser = file.read().split("\n")
        priser = [float(x) for x in priser]
        return priser
    return None

def hent_nedbor(sone):
    with open(f"data/nedbor/{sone}.txt", "r") as file:
        priser = file.read().split("\n")
        priser = [float(x) for x in priser]
        return priser
    return None

def hent_temps(sone):
    with open(f"data/temperatur/{sone}.txt", "r") as file:
        priser = file.read().split("\n")    
        priser = [float(x) for x in priser]
        return priser
    return None

def hovedprogram():
    sonee = {
        "NO1": 1,
        "NO2": 2,
        "NO3": 3,
        "NO4": 4,
        "NO5": 5
    }

    nedbor = []
    temps = []
    soner = []
    priser = []

    for sone in sonee:
        nedboor = hent_nedbor(sone)
        tempss = hent_temps(sone)
        priserr = hent_priser(sone)

        for i in range(len(nedboor)):
            nedbor.append(nedboor[i])
            temps.append(tempss[i])
            priser.append(priserr[i])
            soner.append(sonee[sone])

    values = list(range(len(priser)))

    nedbor = [nedbor[x] for x in values]
    temps = [temps[x] for x in values]
    soner = [soner[x] for x in values]
    priser = [priser[x] for x in values]

    train_nedbor = nedbor[0:2000]
    train_temps = temps[0:2000]
    train_soner = soner[0:2000]
    train_priser = priser[0:2000]

    test_nedbor = nedbor[2000:-1]
    test_temps = temps[2000:-1]
    test_soner = soner[2000:-1]
    test_priser = priser[2000:-1]

    X = np.column_stack((train_nedbor, train_temps, train_soner))    
    Y = np.array(train_priser)

    model = RandomForestRegressor(n_estimators=3)

    model.fit(X, Y)

    sum = 0
    for i in range(len(test_nedbor)):
        predicted = model.predict([[test_nedbor[i], test_temps[i], test_soner[i]]])[0]

        print(f"Predicted: {predicted} og faktisk: {test_priser[i]}")

        if test_priser[i] != 0:
            sum += abs(predicted - test_priser[i]) / test_priser[i]

    gj_sum = sum / len(test_soner)
    print(f"ERROR: {gj_sum}")
    
    pipeline = PMMLPipeline([
        ("regressor", model)
    ])

    pipeline.input_specification = [
        ("input", "float", (3,))
    ]
    
    pipeline.output_specification = [
        ("output", "float")
    ]

    sklearn2pmml(pipeline, "RandomForestRegressor.pmml")


hovedprogram()