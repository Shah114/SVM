"""
Example 2: Non-Linear SVM with RBF Kernel
"""

# Import Modules
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Generate non-linearly separable data using make_circles
from sklearn.datasets import make_circles
x, y = make_circles(n_samples=300, factor=.3, noise=.1)

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Create SVM classifier with RBF kernel
clf = SVC(kernel='rbf', C=1.0, gamma='scale')

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
plt.title("Non-Linear SVM Decision Boundary with RBF Kernel")
plt.show()