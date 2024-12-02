import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if not n_col:
		n_col = np.amax(x) + 1
	matrix = np.zeros([len(x), n_col])
	matrix[np.arange(x.shape[0]), x] = 1
	return matrix
x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)