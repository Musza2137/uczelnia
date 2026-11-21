import random


def rand_elem(array):
    index = random.randint(0, len(array) - 1)
    return array[index]


items = [10, 20, 30, 40, 50]
print(rand_elem(items))
print(rand_elem(items))
print(rand_elem(items))
