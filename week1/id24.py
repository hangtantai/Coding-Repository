import math
from typing import Tuple
def sigmoid(z):
	result = 1 / (1 + math.exp(-z))
	return result
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> Tuple[list[float], float]:
	# Your code here
	j = 0
	linear_unit = []
	for i in range(len(features)):
		unit = 0
		for j in range(len(features[0])):
			unit += features[i][j] * weights[j]
		linear_unit.append(unit + bias)
	probabilities = [round(sigmoid(ele),4) for ele in linear_unit]
	mse = round(sum((prob - label)**2/(len(probabilities)) for prob, label in zip(probabilities, labels)), 4)
	return probabilities, mse

features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1
single_neuron_model(features, labels, weights, bias)
