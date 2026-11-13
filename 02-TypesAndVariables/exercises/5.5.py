price = float(input("price: "))
discount = float(input("discount %: "))
reduction = price * (discount / 100)
discounted_price = price - reduction
print(f"Price with discount: {discounted_price:.2f}")
print(f"Reduction: {reduction:.2f}")
