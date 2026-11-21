t = (10, 20, 30, 40, 50)

print("Tuple:", t)
print("Reverse order:", end=" ")
for i in range(len(t) - 1, -1, -1):
    if i < len(t) - 1:
        print(",", end="")
    print(t[i], end="")
print()
