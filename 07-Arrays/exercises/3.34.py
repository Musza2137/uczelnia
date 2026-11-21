def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def print_2d(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()
    print()


print_2d(identity_matrix(3))
print_2d(identity_matrix(5))
print_2d(identity_matrix(8))
