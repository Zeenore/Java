from random import randint
numbers = [randint(1, 50) for i in range(10)]
print(numbers)
sot = numbers.copy()
print(sot)
sot = sorted(sot)
print(sot)
sot.pop(0)
sot.pop(-1)
print(sum(sot))