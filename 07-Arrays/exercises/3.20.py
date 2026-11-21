arr = [7, 9, 2, 4, 5, 6]

evens = []
odds = []

for num in arr:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

arr = evens + odds
print(arr)
