from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()

X_digits = digits.data
y_digits = digits.target

estimator = PCA(n_components=10)
X_pca = estimator.fit_transform(X_digits)

colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']

for i in range(len(colors)):
    px = X_pca[:, 0][y_digits == i]
    py = X_pca[:, 1][y_digits == i]
    plt.scatter(px, py, c=colors[i])
    plt.legend(digits.target_names)

plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')

# explained variance shows how much information can be attributed to the principle components
print("Explained variance: %s" % estimator.explained_variance_ratio_)

plt.show()
