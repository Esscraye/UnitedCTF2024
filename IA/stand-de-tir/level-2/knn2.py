import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import csv

data_train = pd.read_csv('dataset_train_2.csv')
data_eval = pd.read_csv('dataset_test_2.csv')

X_train = data_train[['x', 'y', 'z']].values
y_train = data_train['score'].values

X_eval = data_eval[['x', 'y', 'z']].values

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

predictions = knn.predict(X_eval)

output_filename = 'predictions.csv'
with open(output_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Score'])
    for prediction in predictions:
        writer.writerow([prediction])

print(f"Predictions saved to {output_filename}")