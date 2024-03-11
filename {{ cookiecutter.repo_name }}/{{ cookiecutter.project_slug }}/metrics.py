from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    fbeta_score,
)
import pandas as pd


def binomial_classification_metrics(
    y_true: pd.Series, y_pred: pd.Series
) -> pd.DataFrame:
    """
    Generate usual binomial classification metrics.

    Args:
        y_true (pd.Series): True values for target.
        y_pred (pd.Series): Predicted values for target.

    Returns:
        pd.DataFrame: Dataframe of metrics.
    """
    metrics = {
        "acc": accuracy_score(y_true=y_true, y_pred=y_pred),
        "precision": precision_score(y_true=y_true, y_pred=y_pred),
        "recall": recall_score(y_true=y_true, y_pred=y_pred),
        "f1": f1_score(y_true=y_true, y_pred=y_pred),
        "f0_5": fbeta_score(y_true=y_true, y_pred=y_pred, beta=0.5),
        "f2": fbeta_score(y_true=y_true, y_pred=y_pred, beta=2),
    }
    return pd.DataFrame(metrics)
