#TCS iON 125 Internship- Research on Artificial Intelligence & Machine Learning powered learning
All the codes to be executed are attached here


1. Implementation code for Intelligent tutors:
The code defines an IntelligentTutor class with three methods: present_concept, present_question, and bkt_update. The present_concept method selects a concept for the student to learn and initializes the student model for that concept. The present_question method selects a question related to the current concept and presents it to the student. 
The student's response is used to update the student model using the BKT algorithm. The bkt_update method implements the BKT algorithm to update the student model.
The code also defines example usage of the IntelligentTutor class, presenting 10 concepts and 3 questions related to each concept. The feedback for the student's responses is provided through a feedback dictionary. The results of the student's responses are printed to the console.


2. Adaptive Learning:
This example uses a neural network model to perform regression on a random dataset, and the learning rate of the optimizer is adjusted dynamically based on the model's performance during training. Specifically, the learning rate is decreased when the loss is low, and increased when the loss is high, allowing the model to adapt to the data more effectively.
Note that this is a simplified example, and the actual implementation of adaptive learning will depend on the specific problem domain and data characteristics. You may need to experiment with different models, optimization algorithms, and hyperparameters to achieve the best results.


3. Dropout prediction:
In this example, synthetic data is generated using the numpy.random.rand() and numpy.random.randint() functions. X represents the features and y represents the target variable. The train_test_split() function from scikit-learn is used to split the dataset into training and testing sets. The logistic regression model is built using the LogisticRegression() function and trained using the fit() method. The predict() method is used to make predictions on the testing set, and the accuracy_score(), precision_score(), recall_score(), and f1_score() functions are used to evaluate the performance of the model.


4. Automation:
Here's an example of an AI and ML algorithm that can generate personalized learning paths for students without using datasets:
In this example, we have defined the Student and Content classes to represent students and learning content, respectively. We have also defined an AI algorithm generate_learning_path() that takes a student and a list of content as inputs and generates a list of recommended content based on the student's knowledge level and interests.
We then generate some sample student and content data and use the generate_learning_path() algorithm to generate personalized learning paths for each student.
Note that the code above is just a sample and may not work out-of-the-box for your specific use case. You would need to customize the algorithm and code according to your specific needs and data.


5. Performance prediction 
The code performs matrix factorization using Singular Value Decomposition (SVD) to predict missing values in the test matrix.

Matrix factorization is a technique used in recommender systems to predict user ratings for items that have not been rated yet. It decomposes a large user-item rating matrix into two smaller matrices, one containing user factors and the other containing item factors. The dot product of these two matrices gives the predicted rating for a user-item pair.

SVD is a popular matrix factorization technique used in recommender systems. It decomposes a matrix into three matrices: U, S, and V, where U and V are orthogonal matrices and S is a diagonal matrix containing singular values. The singular values represent the strength of each latent feature in the original matrix. By selecting a smaller number of singular values, the dimensionality of the original matrix can be reduced, making it easier to compute and more interpretable.

In the code, the user-item matrix is created as a numpy array. Then, the data is split into training and testing sets. The training matrix is converted to float data type and then fed into the svds function from the scipy.sparse.linalg library. The function returns the U, S, and V transpose matrices. The S matrix is converted into a diagonal matrix using the np.diag function.

Finally, the predicted ratings for the test matrix are computed by taking the dot product of the U, S, and V transpose matrices using np.dot. The resulting matrix, X_pred, contains the predicted ratings for all user-item pairs in the test matrix.

The mean squared error (MSE) can be computed between the predicted ratings and the actual ratings in the test matrix using the mean_squared_error function from the sklearn.metrics library. The lower the MSE, the better the model performance.
