import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.metrics import accuracy_score

digits = datasets.load_digits()

images_and_labels = list(zip(digits.images, digits.target))

# to apply a classifier on this data, we need to flatten the image: instead of a 8x8 matrix we
# have to use a one-dimensional array with 64 items
data = digits.images.reshape((len(digits.images), -1))

classifier = svm.SVC(gamma=0.001)

# 75% of the original data-set if for training
train_test_split = int(len(digits.images) * 0.75)
classifier.fit(data[:train_test_split], digits.target[:train_test_split])

# now predict the value of the digit on the 25%
expected = digits.target[train_test_split:]
predicted = classifier.predict(data[train_test_split:])

print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
print(accuracy_score(expected, predicted))

# let's test on the last few images
plt.imshow(digits.images[-3], cmap=plt.cm.gray_r, interpolation='nearest')
print("Prediction for test image: ", classifier.predict(data[-3].reshape(1, -1)))

plt.show()
