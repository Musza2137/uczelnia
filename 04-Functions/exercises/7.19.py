def f(number):
    s = str(abs(number))
    total = 0
    for digit in s:
        if s.count(digit) > 1:
            total += int(digit)
    return total


print(f(1027))
