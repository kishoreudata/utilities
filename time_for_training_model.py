import time
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris


model = MLPClassifier()
X, y = load_iris(return_X_y=True)
start = time.time()
model.fit(X, y)
stop = time.time()
print(f"Training time: {stop - start}s")
# prints: Training time: 0.20307230949401855s