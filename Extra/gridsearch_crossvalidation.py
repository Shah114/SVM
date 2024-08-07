from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Load dataset
iris = datasets.load_iris()
x = iris.data[:, :2] # Only take the first two features.
y = iris.target

# Filter out two classes for binary classification
x = x [y != 2]
y = y [y != 2]

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Define the parameter grid
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [1, 0.1, 0.01, 0.001],
    'kernel': ['rbf', 'poly', 'sigmoid', 'linear']
}

# Create a model
svc = SVC()

# Instantiate the grid search model
grid_search = GridSearchCV(estimator=svc, param_grid=param_grid, cv=5, verbose=1, n_jobs=-1)

# Fit the grid search to the data
grid_search.fit(x_train, y_train)

# Print the best parameters and estimator
print(grid_search.best_params_)
print(grid_search.best_estimator_)