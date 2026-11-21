def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(m[i][j])
        transposed.append(new_row)
    return transposed


def print_2d(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()
    print()


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
m3 = [[5, 6, 7, 8]]

print_2d(transpose_matrix(m1))
print_2d(transpose_matrix(m2))
print_2d(transpose_matrix(m3))
