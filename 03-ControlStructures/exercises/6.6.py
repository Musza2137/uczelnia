hours = int(input("Enter number of parking hours: "))

if hours > 6:
    fee = 20
elif hours >= 3:
    fee = 15
elif hours >= 1:
    fee = 5
else:
    fee = 0

print(f"Parking fee: {fee} PLN")
