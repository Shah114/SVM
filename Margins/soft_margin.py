import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load dataset
iris = datasets.load_iris()
x = iris.data[:, :2] # Only take the first two features.
y = iris.target

# Filter out two classes for binary classification
x = x[y != 2]
y = y[y != 2]

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Create SVM classifier with soft margin
clf = SVC(kernel='linear', C=5) # Soft margin by setting a smaller C value

# Train the classifier
clf.fit(x_train, y_train)

# Plot decision boundary
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='winter')
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
plt.title("Soft Margin SVM Decision Boundary")
plt.show()