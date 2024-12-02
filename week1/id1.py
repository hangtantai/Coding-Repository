def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    if len(a[0]) != len(b):
        return -1
    c = []
    for i in a:
        hold = 0
        for j in range(len(i)):
            hold += i[j] * b[j]
        c.append(hold)

    return c

a = [[1,2],[2,4]]
b = [1,2]
print(matrix_dot_vector(a,b))