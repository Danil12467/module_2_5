def get_matrix(n, m, value):
    matrix=[]
    for i in range(n):
        str = []
        for i in range(m):
            str.append(value)
        matrix.append(str)
    return matrix

result1 = get_matrix(3,10,5)
result2 = get_matrix(2,8,6)
result3 = get_matrix(5,5,3)
print(result1)
print(result2)
print(result3)