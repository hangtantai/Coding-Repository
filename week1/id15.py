import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m, n = X.shape
	theta = np.zeros((n, 1))
	
	for i in range(iterations):
		predictions = X @ theta
		errors = predictions - y.reshape(-1, 1)
		updates = X.T @ errors/m
		theta -= alpha * updates

	theta = np.around(theta, 4)
	return theta

X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000

result = linear_regression_gradient_descent(X, y, alpha, iterations)
print(result)