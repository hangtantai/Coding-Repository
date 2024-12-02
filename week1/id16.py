import numpy as np
from typing import Tuple

def feature_scaling(data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
	# Your code here
	mean = np.mean(data, axis = 0)
	std = np.std(data, axis=0)
	standardization = (data - mean)/std

	max_var = np.max(data, axis = 0)
	min_var = np.min(data, axis = 0)
	normalized_data = (data - min_var)/(max_var - min_var)

	return standardization, normalized_data

data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data))