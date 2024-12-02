import numpy as np

# def shuffle_data(X, y, seed=None):
# 	# Your code here
# 	if seed != None:
# 		np.random.shuffle(X)
# 		np.random.shuffle(y)
# 	return X, y

import numpy as np

def shuffle_data(X, y, seed=None):
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]
X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8]])
y = np.array([1, 2, 3, 4])
print(shuffle_data(X, y, 59))

