def flatten_2d(arr_2d):
    arr_1d = []
    for row in arr_2d:
        for val in row:
            arr_1d.append(val)
    return arr_1d


a1 = [[2, 3], [1, 5]]
a2 = [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]
a3 = [[2, 1], [3, 5], [7, 4], [2, 6]]

print(flatten_2d(a1))
print(flatten_2d(a2))
print(flatten_2d(a3))
