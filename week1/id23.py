import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
	sum_exp = sum([math.exp(score) for score in scores])
	probabilities = []
	for score in scores:
		probabilities.append(round(math.exp(score)/sum_exp, 4))
	return probabilities

scores = [1, 2, 3]
result = softmax(scores)
print(result)