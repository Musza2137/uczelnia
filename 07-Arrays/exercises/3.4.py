arr = [-15, 8, -31, 47, -2, 19]

minimum = arr[0]
maximum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("Array:", arr)
print("Minimum:", minimum)
print("Maximum:", maximum)
