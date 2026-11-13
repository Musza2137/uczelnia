###
# A program that reads an integer number from the keyboard
# and prints that value as a binary and hexadecimal number.
#
number = int(input("Enter number: "))
binary_number = bin(number)
hex_number = hex(number)

print(f"Binary number: {binary_number}")
print(f"Hexadecimal number: {hex_number}")
