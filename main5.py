# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11
number: float = input("Введите дробное число: ")
def sum_digits_numbers(n):
    str_n = str(n)
    str_n = str_n.replace('.', '')
    lst_n = list(str_n)
    lst_num = map(int, lst_n)
    summa = sum(lst_num)
    print(f'{number} -> {summa}')
sum_digits_numbers(number)





