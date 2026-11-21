def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    a = 0
    b = 1
    for i in range(n - 2):
        next_val = a + b
        a = b
        b = next_val
    return b


print(f(9))
