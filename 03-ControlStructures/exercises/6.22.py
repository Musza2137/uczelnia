###
# Prints numbers from 1 to 30, replacing multiples of 3 with 'THREE',
# multiples of 5 with 'FIVE', and multiples of both 3 and 5 with 'BINGO'
#
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("BINGO", end=" ")
    elif i % 3 == 0:
        print("THREE", end=" ")
    elif i % 5 == 0:
        print("FIVE", end=" ")
    else:
        print(i, end=" ")
