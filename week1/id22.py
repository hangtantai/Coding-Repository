import math

def sigmoid(z: float) -> float:
	#Your code here
	
    # sigmoid = 1/( 1 + exp(-z))
	result = 1/ ( 1 + math.exp(-z))
	return round(result,4)

z = 0
print(sigmoid(z))