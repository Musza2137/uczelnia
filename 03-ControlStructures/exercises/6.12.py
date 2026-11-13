products_count = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

if products_count <= 2:
    amount_to_pay = products_count * product_price
else:
    amount_to_pay = (2 * product_price) + ((products_count - 2) * product_price * 0.75)

print(f"Amount to pay: {amount_to_pay:.2f}")
