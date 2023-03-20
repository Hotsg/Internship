# Performance prediction

import numpy as np
from sklearn.metrics import mean_squared_error
from scipy.sparse.linalg import svds

# Create user-item matrix
ratings_matrix = np.array([[4, 5, 0, 2],
                           [3, 0, 4, 3],
                           [0, 4, 3, 0],
                           [5, 2, 0, 4]])

# Split data into training and testing sets
train_matrix = np.array([[4, 5, 0, 0],
                         [3, 0, 4, 0],
                         [0, 4, 3, 0],
                         [0, 2, 0, 4]])
test_matrix = np.array([[0, 0, 0, 2],
                        [0, 0, 0, 3],
                        [0, 0, 0, 0],
                        [5, 0, 0, 0]])

# Convert train matrix to float data type
train_matrix = train_matrix.astype(float)

# Perform matrix factorization
u, s, vt = svds(train_matrix, k=2)
s_diag_matrix = np.diag(s)
X_pred = np.dot(np.dot(u, s_diag_matrix), vt)

# Evaluate model performance on testing data
test_preds = X_pred[test_matrix.nonzero()].flatten()
test_truth = test_matrix[test_matrix.nonzero()].flatten()
mse = mean_squared_error(test_truth, test_preds)
rmse = np.sqrt(mse)
print('RMSE:', rmse)

# Make personalized recommendations
user_id = int(input("Enter the user_id: "))
user_ratings = ratings_matrix[user_id-1,:]
user_preds = X_pred[user_id-1,:]
recommendations = np.argsort(-user_preds)[:10]
print('Recommendations for User', user_id)
print(recommendations)


