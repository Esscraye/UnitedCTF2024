import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import csv

def custom_distance(p1, p2):
    return (np.abs(p1[0] - p2[0]) +
            2 * np.abs(p1[1] - p2[1]) +
            (p1[2] - p2[2]) ** 2 +
            np.abs(p1[3] - p2[3]) +
            (p1[4] - p2[4]) ** 2 +
            np.abs(p1[5] - p2[5]) +
            4 * np.abs(p1[6] - p2[6]) +
            np.abs(p1[7] - p2[7]))

class CustomKNN(KNeighborsClassifier):
    def __init__(self, n_neighbors=5):
        super().__init__(n_neighbors=n_neighbors, metric='pyfunc', metric_params={'func': custom_distance})

data_train = pd.read_csv('dataset_train_3.csv')
data_eval = pd.read_csv('dataset_test_3.csv')


X_train = data_train.iloc[:, :-1].values 
y_train = data_train.iloc[:, -1].values   

X_eval = data_eval.values  

knn = CustomKNN(n_neighbors=3)
knn.fit(X_train, y_train)

predictions = knn.predict(X_eval)

output_filename = 'predictions.csv'
with open(output_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Score'])
    for prediction in predictions:
        writer.writerow([prediction])

print(f"Predictions saved to {output_filename}")