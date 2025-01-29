import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate

# logistic regression accuracy: 93%
# we do better with knn: 97.5% !!!!!!!!
# 84% simple kNN without normalizing the dataset
# we can achieve ~ 99% with random forests

credit_data = pd.read_csv("credit_data.csv")

features = credit_data[["income", "age", "loan"]]
targets = credit_data.default

# machine learning handle arrays not data-frames
X = np.array(features).reshape(-1, 3)
y = np.array(targets)

model = RandomForestClassifier()
predicted = cross_validate(model, X, y, cv=10)

print(np.mean(predicted['test_score']))
