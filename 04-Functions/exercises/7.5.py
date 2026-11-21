import range_check

num = int(input("A number: "))
if range_check.in_range(num, 2, 15):
    result = "yes"
else:
    result = "no"

print(f"Number {num} in the range <2,15>: {result}")
