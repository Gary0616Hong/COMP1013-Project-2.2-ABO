import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, classification_report

def metric_row(name, y_true, y_pred):
    return {
        "model": name,
        "accuracy": accuracy_score(y_true, y_pred),
        "macro_f1": f1_score(y_true, y_pred, average="macro"),
        "weighted_f1": f1_score(y_true, y_pred, average="weighted"),
    }

def per_class_table(y_true, y_pred):
    return pd.DataFrame(classification_report(y_true, y_pred, output_dict=True)).T
