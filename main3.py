from random import randint
numbers = [randint(1, 15) for i in range(5)]
print(numbers)
sot = numbers.copy()
sot = sorted(sot)
print(sot)
sot.pop(0)
sot.pop(-1)
print(sum(sot))