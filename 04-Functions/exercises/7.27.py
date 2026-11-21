def f(product_code):
    digits_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    control_digit = int(product_code[3])
    return digits_sum % 7 == control_digit


print(f("1082"))
