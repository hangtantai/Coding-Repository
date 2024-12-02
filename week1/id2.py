def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    return [list(i) for i in zip(*a)]

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    rows = len(a)
    cols = len(a[0])

    matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            matrix[j][i] = a[i][j]
    return matrix

a = [[1,2,3],[4,5,6]]
print(transpose_matrix(a))
