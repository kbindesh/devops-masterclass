import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as cluster_algorithm
from sklearn.cluster import AgglomerativeClustering

shopping_data = pd.read_csv('shopping_data.csv')
