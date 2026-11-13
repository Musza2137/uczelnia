###
# Determines the quadrant or axis of a point P(x, y) in the coordinate system
#
x = 5
y = 2

print(f"x = {x}")
print(f"y = {y}")

if x == 0 and y == 0:
    print(f"Point P({x},{y}) is located in the position (0,0) of the coordinate system")
elif x == 0:
    print(f"Point P({x},{y}) is located on the y-axis")
elif y == 0:
    print(f"Point P({x},{y}) is located on the x-axis")
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
else:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
