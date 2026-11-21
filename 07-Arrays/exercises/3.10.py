arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

for num in arr1:
    found = False
    for item in arr2:
        if num == item:
            found = True
            break
    if not found:
        print(num, end=" ")
print()
