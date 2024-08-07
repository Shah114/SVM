# SVM
Classification 
<br/>

**Support Vector Machines (SVM)** are a set of supervised learning methods used for **classification, regression, and outliers detection**. Developed by Vladimir Vapnik and his colleagues, SVMs are powerful tools capable of performing **linear and non-linear classification**. They are known for their **robustness in high-dimensional spaces** and **effectiveness** in cases where the number of dimensions exceeds the number of samples. <br/>
<br/>

**Key Concepts**:
* **Support Vectors**: The data points that are closest to the decision boundary. These points are critical in defining the position of the boundary.
* **Hyperplane**: A decision boundary that separates different classes. In two dimensions, it is a line; in three dimensions, a plane.
* **Margin**: The distance between the hyperplane and the nearest data point from either class. <br/>
<br/>

**Applications of SVM**:
* **Image Classification**: SVMs are used in image recognition and classification tasks.
* **Bioinformatics**: They are used for classifying genes, proteins, and other biological data.
* **Text Categorization**: SVMs classify documents into categories such as spam and non-spam emails.
* **Handwriting Recognition**: SVMs classify handwritten characters. <br/>
<br/>

**Linear SVM** <br/>
In the simplest form, SVM is a linear classifier. Given a set of training data, the algorithm finds a hyperplane that best separates the data into classes. <br/>
**Objective**: Maximize the margin between the two classes. <br/>
<br/>

**Non-Linear SVM** <br/>
When data is not linearly separable, SVM can be extended using the kernel trick. The idea is to transform the input space into a higher-dimensional space where a linear separation is possible.
For instance, in a 2D space, points that form a circle can be linearly separable in a 3D space after a suitable transformation. <br/>
<br/>

**Kernel Trick** <br/>
The kernel trick is a fundamental concept in Support Vector Machines (SVM) that allows for efficient classification and regression in complex, non-linearly separable data spaces. It involves transforming data into a higher-dimensional space where a linear separation can be achieved, without explicitly performing the transformation. <br/>

Kernels are functions that take the input data and transform it into a higher-dimensional space. This allows SVM to create non-linear boundaries. <br/>
**Choosing the Right Kernel**:
* **Linear Kernel**: Best used when the data is linearly separable.
* **Polynomial Kernel**: Useful for image processing and other applications where interactions between features are important.
* **RBF Kernel**: Widely used in SVM classification because it can handle the case when the relation between class labels and attributes is non-linear.
* **Sigmoid Kernel**: Sometimes used as an alternative to neural networks. <br/>
<br/>

**Soft Margin and Hard Margin** <br/>
1. **Hard Margin** <br/>
Hard Margin SVMs aim to find a hyperplane that perfectly separates the data into different classes with no misclassification. This approach assumes that the data is linearly separable, meaning that there exists a hyperplane that can divide the classes without any errors. <br/>

* Objective: Maximize the margin between the classes while ensuring that all data points are correctly classified.
* Constraints: The hard margin SVM imposes strict constraints on the data, such that no data point can fall on the wrong side of the margin.
* Applicability: Hard margin SVMs are used when the dataset is linearly separable and there is no noise in the data. <br/>

2. **Soft Margin** <br/>
Soft Margin SVMs, introduced by the C parameter, allow for some misclassification of data points to achieve a more robust model when the data is not linearly separable or contains noise. This approach is designed to handle real-world scenarios where perfect separation is not possible. <br/>

* Objective: Maximize the margin between classes while allowing some data points to be within the margin or misclassified.
* Constraints: Soft margin SVMs use a relaxation of the hard margin constraints to allow for some errors. This is controlled by a regularization parameter 
𝐶, which determines the trade-off between maximizing the margin and minimizing the classification error.
* Applicability: Soft margin SVMs are used when dealing with noisy data or when the data is not perfectly linearly separable. <br/>
<br/>

Grid Search and Cross-Validation are essential techniques in machine learning for optimizing model performance and ensuring robust evaluation. Here's a detailed overview of both: <br/>
**Grid Search** <br/>
Grid Search is a hyperparameter optimization technique used to find the best set of hyperparameters for a given machine learning model. Hyperparameters are parameters that are not learned from the training data but are set before the training process begins, such as the number of trees in a Random Forest or the regularization strength in an SVM. <br/>
* Objective: To systematically explore a predefined set of hyperparameter values to determine the combination that yields the best model performance.
* Process:
1. Define Parameter Grid: Create a grid of hyperparameter values to be tested. For example, if tuning an SVM, you might include various values for the regularization parameter 
𝐶 and different kernel functions.
2. Train and Evaluate: Train the model using each combination of hyperparameters and evaluate its performance using a specified metric (e.g., accuracy, F1-score).
3. Select Best Parameters: Identify the hyperparameter combination that results in the best performance based on the evaluation metric. <br/>
<br/>

**Cross-Validation** <br/>
Cross-Validation is a technique used to assess how well a model generalizes to unseen data. It involves partitioning the dataset into multiple subsets or "folds" and using different combinations of these folds for training and validation. <br/>
* Objective: To estimate the model’s performance and ensure that it generalizes well to new, unseen data by using different subsets of the dataset for training and testing.
* Process:
1. Split Data: Divide the dataset into 𝑘 folds (typically 5 or 10).
2. Train and Validate: For each fold, train the model on 𝑘 − 1 folds and validate it on the remaining fold. This process is repeated 𝑘 times, with each fold being used as the validation set once.
3. Evaluate Performance: Calculate performance metrics (e.g., accuracy, precision) for each fold and average the results to get a final estimate of the model’s performance. <br/>
<br/>

Types: <br/>
* k-Fold Cross-Validation: The dataset is split into 𝑘 folds. Each fold is used once as a validation set while the remaining 𝑘 − 1 folds are used for training.
* Stratified k-Fold Cross-Validation: Ensures that each fold has a representative distribution of the target classes, which is particularly useful for imbalanced datasets.
* Leave-One-Out Cross-Validation (LOOCV): A special case of k-Fold Cross-Validation where 𝑘 is equal to the number of samples in the dataset. Each sample is used as a validation set once while the remaining samples are used for training.


 




