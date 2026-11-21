def occurs(number, array):
    for item in array:
        if item == number:
            return True
    return False


arr = [15, 38, 7, 23, 14]
num = int(input("Number: "))

print("Array:", end=" ")
for x in arr:
    print(x, end=" ")
print()

if occurs(num, arr):
    print(f"Result: number {num} appears in the array")
else:
    print(f"Result: number {num} does not appear in the array")
