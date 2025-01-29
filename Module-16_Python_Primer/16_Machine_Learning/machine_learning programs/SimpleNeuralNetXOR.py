from keras.models import Sequential
from keras.layers.core import Dense
import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

model = Sequential()
model.add(Dense(4, input_dim=2, activation='sigmoid'))
model.add(Dense(1, input_dim=4, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
model.fit(X, y, epochs=30000, verbose=2)

print("Predictions after the training ...")
print(model.predict(X))
