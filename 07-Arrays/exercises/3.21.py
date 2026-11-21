arr1 = [3, 5, 1]
arr2 = [1, 2, 3, 4, 5, 6]

is_subset = True
for item1 in arr1:
    found = False
    for item2 in arr2:
        if item1 == item2:
            found = True
            break
    if not found:
        is_subset = False
        break

print("Is arr1 a subset of arr2?", is_subset)
