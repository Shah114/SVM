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



