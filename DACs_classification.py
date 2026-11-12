"""
CSE 5120 - Assignment 1: Classification of Disadvantaged Communities (DACs)

Complete every function marked TODO. Keep the function names, their arguments,
and what they return exactly as described: Gradescope imports this file and
calls each function separately, so a function that is not finished only loses
the points for that function.

Run this file (python DACs_classification.py) to train both models, print
their results, and save SvmClassifier.sav and RfClassifier.sav.

Do not change the constants below. Put any code you want to run yourself
inside main(); do not add code that runs at the top level of the file.
"""

# Step 1: Import libraries
# pandas is imported for you. Add the other imports you need here
# (for example pickle, category_encoders, and the scikit-learn classes).
import pandas as pd


DATA_FILE = "disadvantaged_communities.csv"   # keep this file in the same folder
TARGET = "CES 4.0 Percentile Range"           # the column the models predict
CATEGORICAL_COLUMNS = ["California County", "Approximate Location", "DAC category"]
SVM_MODEL_FILE = "SvmClassifier.sav"
RF_MODEL_FILE = "RfClassifier.sav"


# Step 2: Load the dataset
def load_dataset(path=DATA_FILE):
    """Read the CSV file at `path` and return it as a pandas DataFrame.

    Return the data exactly as it is in the file (2284 rows, 59 columns).
    """
    # TODO: write your code here
    raise NotImplementedError("load_dataset is not implemented yet")


def describe_dataset(df):
    """Print basic statistics for your report (this function is not graded).

    1. Dataset size (dimensions)
    2. Column names
    3. Distribution of the target column (TARGET)
    4. Percentage distribution of the target column
    """
    # TODO: write your code here
    pass


# Step 3: Clean the dataset
def clean_dataset(df):
    """Return a copy of `df` that has no missing values.

    Use ONE of these two methods:
      - replace each missing value with the mean of its column, or
      - remove the rows that have missing values.
    """
    # TODO: write your code here
    raise NotImplementedError("clean_dataset is not implemented yet")


# Step 4: Encode the categorical variables
def encode_categorical(df):
    """Return a copy of `df` in which the columns listed in CATEGORICAL_COLUMNS
    are encoded as ordinal integers (one integer per category).

    Use OrdinalEncoder from the category_encoders library, for example
    category_encoders.OrdinalEncoder(cols=CATEGORICAL_COLUMNS).
    Keep all rows and all columns; only the values of those columns change.
    You may leave the TARGET column as text.
    """
    # TODO: write your code here
    raise NotImplementedError("encode_categorical is not implemented yet")


# Step 5: Separate predictors from the target and create the train/test split
def split_dataset(df):
    """Split the cleaned, encoded DataFrame into training and test sets.

    X is every column except TARGET; y is the TARGET column.
    Use train_test_split with test_size=0.2, random_state=0 and stratify=y
    (an 80% / 20% split with the same class balance in both parts).

    Return X_train, X_test, y_train, y_test (in this order).
    """
    # TODO: write your code here
    raise NotImplementedError("split_dataset is not implemented yet")


# Step 6: Standardize the features (needed for the SVM only, not for Random Forest)
def scale_features(X_train, X_test):
    """Standardize the features with StandardScaler.

    Fit the scaler on X_train only, then transform both X_train and X_test
    with it. Return X_train_scaled, X_test_scaled (in this order).
    """
    # TODO: write your code here
    raise NotImplementedError("scale_features is not implemented yet")


# Step 7: Build and train the SVM classifier
def train_svm(X_train_scaled, y_train):
    """Create an SVC with these parameters, train it, and return it:

      1. RBF kernel
      2. C = 10.0
      3. gamma = 0.3
    """
    # TODO: write your code here
    raise NotImplementedError("train_svm is not implemented yet")


# Step 8: Build and train the Random Forest classifier
def train_random_forest(X_train, y_train):
    """Create a RandomForestClassifier with n_estimators=10 and random_state=0,
    train it on the features that are NOT standardized, and return it.
    """
    # TODO: write your code here
    raise NotImplementedError("train_random_forest is not implemented yet")


# Step 9: Precision, recall and specificity from a confusion matrix
def compute_metrics(cm):
    """Return precision, recall, specificity (in this order) for a confusion
    matrix `cm` as produced by sklearn.metrics.confusion_matrix
    (rows = actual classes, columns = predicted classes).

    This dataset has 10 classes, so compute each metric per class and then
    average over the classes (macro average). For class k:

        TP = cm[k, k]
        FP = (sum of column k) - TP
        FN = (sum of row k) - TP
        TN = (sum of the whole matrix) - TP - FP - FN

        precision_k   = TP / (TP + FP)
        recall_k      = TP / (TP + FN)
        specificity_k = TN / (TN + FP)

    If a denominator is 0 for a class, use 0 for that class.
    Each returned value is the mean of the per-class values.
    """
    # TODO: write your code here
    raise NotImplementedError("compute_metrics is not implemented yet")


# Step 10: Save a trained model
def save_model(model, filename):
    """Save `model` to the file `filename` using the pickle library."""
    # TODO: write your code here
    raise NotImplementedError("save_model is not implemented yet")


def main():
    """Run the whole assignment. Use the output in your report.

    1. Load the dataset and print its statistics (describe_dataset).
    2. Clean it, encode it, split it, and standardize the features.
    3. Train the SVM on the standardized training data, then print its
       confusion matrix, accuracy score, precision, recall and specificity
       on the standardized test data. Save it as SVM_MODEL_FILE.
    4. Train the Random Forest on the training data that is NOT standardized,
       print the same results on the test data, and save it as RF_MODEL_FILE.
    """
    # TODO: write your code here
    pass


if __name__ == "__main__":
    main()
