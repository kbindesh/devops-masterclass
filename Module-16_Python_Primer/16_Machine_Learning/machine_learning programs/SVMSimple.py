import numpy as np
from matplotlib import pyplot as plt
from sklearn import svm
from mlxtend.plotting import plot_decision_regions

x_blue = np.array([0.5, 1, 1.4, 1.7, 2])
y_blue = np.array([4.5, 2.3, 1.9, 8.9, 4.1])

x_red = np.array([0.3, 3.3, 3.5, 4, 4.4, 5.7, 6])
y_red = np.array([1, 7, 1.5, 6.3, 1.9, 2.9, 7.1])

X = np.array(
    [[0.3, 1], [0.5, 4.5], [1, 2.3], [1.4, 1.9], [1.7, 8.9], [2, 4.1], [3.3, 7], [3.5, 1.5], [4, 6.3], [4.4, 1.9],
     [5.7, 2.9], [6, 7.1]])
y = np.array([1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # 0: blue class, 1: red class

plt.plot(x_blue, y_blue, 'ro', color='blue')
plt.plot(x_red, y_red, 'ro', color='red')
plt.plot(4.5, 4.5, 'ro', color='green')

"""
#	Important parameters for SVC: gamma and C
#		gamma -> defines how far the influence of a single training example reaches
#					Low value: influence reaches far      High value: influence reaches close
#
#		C -> trades off hyperplane surface simplicity + training examples mis-classification
#					Low value: simple/smooth hyperplane surface 
#					High value: all training examples classified correctly but complex surface 
"""

classifier = svm.SVC(C=10)
classifier.fit(X, y)

print(classifier.predict([[4.5, 4.5]]))

plot_decision_regions(X, y, clf=classifier, legend=2)

plt.axis([-0.5, 10, -0.5, 10])
plt.show()

