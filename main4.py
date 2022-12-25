n = int(input("Введите число: "))
print("Ваша последовательность: ")
def f(n1):
    for i in range(1, n1 + 1):
        print((-3) ** (i -1), end = ',')
f(n)