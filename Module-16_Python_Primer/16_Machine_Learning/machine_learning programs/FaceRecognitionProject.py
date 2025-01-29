from sklearn.datasets import fetch_olivetti_faces
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn import metrics
import numpy as np

olivetti_data = fetch_olivetti_faces()

# there are 400 images - 10x40 (40 people - 1 person has 10 images) - 1 image = 64x64 pixels
features = olivetti_data.data
# we represent target variables (people) with integers (face ids)
targets = olivetti_data.target

# split the original data-set (training and test set)
X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.25, stratify=targets, random_state=0)

# let's try to find the optimal number of eigenvectors (principle components)
pca = PCA(n_components=100, whiten=True)
pca.fit(X_train)
X_pca = pca.fit_transform(features)

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

# let's use the machine learning models

models = [("Logistic Regression", LogisticRegression()), ("Support Vector Machine", SVC()), ("Naive Bayes Classifier", GaussianNB())]

for name, model in models:

    kfold = KFold(n_splits=5, shuffle=True, random_state=0)
    cv_scores = cross_val_score(model, X_pca, targets, cv=kfold)
    print("Mean of the cross-validation scores: %s" % cv_scores.mean())



