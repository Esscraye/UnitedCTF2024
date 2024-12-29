import csv
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def load_csv(filename, has_target=True):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        data = [list(map(float, row)) for row in reader]
    if has_target:
        data = np.array(data)
        return data[:, :-1], data[:, -1]
    else:
        return np.array(data)

def save_predictions(predictions, output_filename):
    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Score'])
        for prediction in predictions:
            writer.writerow([prediction])

train_data, train_scores = load_csv('dataset_train_1.csv')
eval_data = load_csv('dataset_test_1.csv', has_target=False)

k = 3

knn_regressor = KNeighborsRegressor(n_neighbors=k)
knn_regressor.fit(train_data, train_scores)

predictions = knn_regressor.predict(eval_data)

save_predictions(predictions, 'predictions.csv')