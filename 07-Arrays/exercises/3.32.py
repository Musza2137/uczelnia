arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [2, 4, 6, 8, 1]]

print("Before:")
for row in arr:
    for val in row:
        print(val, end=" ")
    print()

temp = arr[0]
arr[0] = arr[len(arr) - 1]
arr[len(arr) - 1] = temp

print("\nAfter:")
for row in arr:
    for val in row:
        print(val, end=" ")
    print()
