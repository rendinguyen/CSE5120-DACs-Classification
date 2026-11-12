"""
CSE 5120 - Assignment 1: evaluation of your saved DACs classifiers

Complete every function marked TODO. Keep the function names, their arguments,
and what they return exactly as described.

Run DACs_classification.py first so that SvmClassifier.sav and RfClassifier.sav
exist, then run this file (python evaluation.py) and use the output in your report.
"""

# 1. Import any library you need (for example pickle and the metric functions
#    from scikit-learn). You can reuse your own functions and constants:
from DACs_classification import (RF_MODEL_FILE, SVM_MODEL_FILE, clean_dataset,
                                 compute_metrics, encode_categorical, load_dataset,
                                 scale_features, split_dataset)


# 2. Load a saved model
def load_model(filename):
    """Load and return the model that was saved in `filename` with pickle."""
    # TODO: write your code here
    raise NotImplementedError("load_model is not implemented yet")


# 3. Evaluate a model on a test set
def evaluate_model(model, X_test, y_test):
    """Make predictions for X_test and compare them with y_test.

    Return a dictionary with exactly these keys:
        "confusion_matrix": the matrix from sklearn.metrics.confusion_matrix(y_test, y_pred)
        "accuracy":         the accuracy score (a number between 0 and 1)
        "precision":        from your compute_metrics function
        "recall":           from your compute_metrics function
        "specificity":      from your compute_metrics function
    """
    # TODO: write your code here
    raise NotImplementedError("evaluate_model is not implemented yet")


def main():
    """Evaluate both saved models and print the results.

    1. Recreate the test set with your functions from DACs_classification.py
       (load, clean, encode, split, and scale the features for the SVM).
    2. Load SVM_MODEL_FILE and evaluate it on the standardized test features.
    3. Load RF_MODEL_FILE and evaluate it on the test features that are NOT standardized.
    4. For each model print the confusion matrix, accuracy score, precision,
       recall and specificity.
    """
    # TODO: write your code here
    pass


if __name__ == "__main__":
    main()
