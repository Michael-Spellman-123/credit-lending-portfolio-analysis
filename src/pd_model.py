                 
from sklearn.linear_model import LogisticRegression

class PDModel:
    def __init__(self):
        self.model = LogisticRegression(max_iter=200)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict_proba(self, X):
        return self.model.predict_proba(X)[:, 1]
