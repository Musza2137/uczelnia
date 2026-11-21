def f(n):
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        is_prime = True
        for i in range(2, candidate):
            if candidate % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return candidate


print(f(5))
