import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.base import clone

model = LogisticRegression()
def fit_logistic(X,y):
    model_ = clone(model)
    model_.fit(X,y)
    return model_

