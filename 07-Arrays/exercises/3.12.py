arr = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:", end=" ")
for x in arr:
    print(x, end=" ")
print()

print("Unique elements:", end=" ")
for x in arr:
    if arr.count(x) == 1:
        print(x, end=" ")
print()
