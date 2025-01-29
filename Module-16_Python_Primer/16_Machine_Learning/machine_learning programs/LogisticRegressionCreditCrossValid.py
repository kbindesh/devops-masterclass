import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate

credit_data = pd.read_csv("credit_data.csv")

features = credit_data[["income", "age", "loan"]]
target = credit_data.default

# machine learning handle arrays not data-frames
X = np.array(features).reshape(-1, 3)
y = np.array(target)

model = LogisticRegression()
predicted = cross_validate(model, X, y, cv=10)

print(np.mean(predicted['test_score']))
