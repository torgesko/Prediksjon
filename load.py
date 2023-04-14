from sklearn2pmml import sklearn2pmml
from sklearn2pmml import PMMLPipeline
import numpy as np

pipeline = PMMLPipeline.fromPMML("RandomForestRegressor.pmml")

# create sample input data
X_test = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# make predictions using the loaded model
y_pred = pipeline.predict(X_test)

# print the predictions
print(y_pred)
