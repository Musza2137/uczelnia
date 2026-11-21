arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [2, 4, 6, 8, 1]]

print("Before:")
for row in arr:
    for val in row:
        print(val, end=" ")
    print()

for i in range(len(arr)):
    last_col = len(arr[i]) - 1
    temp = arr[i][0]
    arr[i][0] = arr[i][last_col]
    arr[i][last_col] = temp

print("\nAfter:")
for row in arr:
    for val in row:
        print(val, end=" ")
    print()
