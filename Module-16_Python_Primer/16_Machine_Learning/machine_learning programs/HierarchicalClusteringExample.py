import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

x = np.array([[1, 1], [1.5, 1], [3, 3], [4, 4], [3, 3.5], [3.5, 4]])

plt.scatter(x[:, 0], x[:, 1], s=50)
plt.show()

linkage_matrix = linkage(x, "single")

dendrogram = dendrogram(linkage_matrix, truncate_mode='none')

plt.title("Hierarchical Clustering")
plt.show()