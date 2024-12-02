import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	C = np.array(C)
	B = np.array(B)

	inverse_C = np.linalg.inv(C)
	P = B.dot(inverse_C)
	P = np.around(P, 4)
	return P

	# Concept: B = P*C => B*C^-1 = P
B = [[1, 0, 0], 
	[0, 1, 0], 
	[0, 0, 1]]
C = [[1, 2.3, 3], 
	[4.4, 25, 6], 
	[7.4, 8, 9]]
print(transform_basis(B,C))