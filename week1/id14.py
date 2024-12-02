import numpy as np
# https://www.geeksforgeeks.org/ml-normal-equation-in-linear-regression/
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X_np = np.array(X)
    y_np = np.array(y)
    
    X_transpose = np.transpose(X_np)
    theta = np.linalg.inv(X_transpose.dot(X_np)).dot(X_transpose).dot(y_np)
    
    return theta.tolist()