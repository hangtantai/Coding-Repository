import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	n_samples = X.shape[0]
	batches = []
	for i in np.arange(0, n_samples, batch_size):
		begin, end = i, min(i + batch_size, n_samples)
		if y is not None:
			batches.append([X[begin:end], y[begin:end]])
		else:
			batches.append(X[begin:end])
	return batches

X = np.array([[1, 2], 
			[3, 4], 
			[5, 6], 
			[7, 8], 
			[9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
print(batch_iterator(X, y, batch_size))