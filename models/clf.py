from typing import Any
import numpy.typing as npt
from sklearn.linear_model import LogisticRegression

def fit_logistic(
    X: npt.ArrayLike,
    y: npt.ArrayLike,
    **kwargs: Any
) -> LogisticRegression:
    """Fit a logistic regression model to the given data.

    Args:
        X: Feature matrix
        y: Target vector
        **kwargs: Additional parameters passed to LogisticRegression

    Returns:
        Fitted LogisticRegression model
    """
    model = LogisticRegression(**kwargs)
    return model.fit(X, y)


