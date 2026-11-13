###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Read temperature in degrees Celsius from the keyboard
celsius = float(input("Enter temperature in degrees Celsius: "))

# Calculate temperature in Kelvin and Fahrenheit
kelvin = celsius + 273.15
fahrenheit = (celsius * 9 / 5) + 32

# Print the results
print(f"Temperature in Kelvin: {kelvin}")
print(f"Temperature in Fahrenheit: {fahrenheit}")
