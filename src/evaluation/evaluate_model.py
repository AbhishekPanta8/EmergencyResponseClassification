import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def evaluate_model(preds, labels):
    """
    Evaluate the model with accuracy, precision, recall, and F1 score.
    """
    acc = accuracy_score(labels, preds)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='weighted')
    return {
        'accuracy': acc,
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }
