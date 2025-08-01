What Is Supervised Learning?
Supervised Learning is a type of machine learning where you train a model using a labeled dataset — where the input (X) and the correct output (Y) are both provided.

The model learns the pattern between X and Y so it can predict Y for new X.

 Supervised Learning Flow
Step-by-step:
You collect labeled data

Example: Emails with label spam/not spam

Split the data

80% → Training data

20% → Testing data

Train a model

It learns from (X → Y)

Make predictions

Use model to predict labels for new data

Evaluate the model

Using accuracy, precision, recall, etc.

| Type               | Goal                        | Output Example      |
| ------------------ | --------------------------- | ------------------- |
| **Classification** | Predict a category/label    | Spam or Not Spam    |
| **Regression**     | Predict a continuous number | ₹ Price, Age, Score |


Classification vs Regression — Explained
🟢 Classification:
Output is a label (discrete)

Models: Logistic Regression, Decision Tree, SVM, Random Forest, etc.
Input: "Win a free iPhone!"
Output: Spam

 Regression:
Output is a number (continuous)

Models: Linear Regression, Ridge, Lasso, SVR
 Example:
 Input: House with 2BHK, 1200 sqft
Output: ₹32,50,000

Common Supervised Learning Algorithms :

| Algorithm              | Type           | Description                               |
| ---------------------- | -------------- | ----------------------------------------- |
| Linear Regression      | Regression     | Fits a line to predict numbers            |
| Logistic Regression    | Classification | Predicts yes/no using a probability curve |
| Decision Trees         | Both           | Makes if-else rules                       |
| Random Forest          | Both           | Group of trees (more accurate)            |
| K-Nearest Neighbors    | Both           | Uses nearby points to guess               |
| Support Vector Machine | Classification | Draws boundary between categories         |
| Naive Bayes            | Classification | Great for text data                       |
| Neural Networks        | Both           | Used for images, voice, language, etc.    |
