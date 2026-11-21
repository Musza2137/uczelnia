t = (50, 20, 40, 50, 30, 50)
val = 50

count = 0
for item in t:
    if item == val:
        count += 1

print("Tuple:", t)
print("Value:", val)
print("Number of occurrences:", count)
