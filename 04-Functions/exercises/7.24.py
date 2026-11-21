def f(expression):
    total = int(expression[0])
    operator = "+"

    for char in expression[1:]:
        if char == "+" or char == "-":
            operator = char
        else:
            if operator == "+":
                total += int(char)
            elif operator == "-":
                total -= int(char)

    return total


print(f("2+3-4+5-0"))
