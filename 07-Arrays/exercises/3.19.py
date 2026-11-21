arr = [4.5, 12.1, 3.0, 8.7, 15.2, 6.4]
threshold = float(input("Enter a value: "))

count = 0
for num in arr:
    if num > threshold:
        count += 1

print("Number of elements greater than", threshold, ":", count)
