#  1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
#  ['gfh5', 'gfh2', '67', 'jy32', '3put']
# a = input()
# num_list = []

# num = ''
# for char in a:
#     if char.isdigit():
#         num = num + char
#     else:
#         if num != '':
#             num_list.append(int(num))
#             num = ''
# if num != '':
#     num_list.append(int(num))

# print(*num_list)
# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


# a = ["qwe", "asd", "zxc", "qwe", "ertqwe", "asd", "ertqwe"]
# str = input("Ну что? Начнем поиск) ")
# for i in a:
#     if str in a:
#         print(f'Нашел одну коппию позиция по индексу -> {a.index(str, 2)}')
#         break
#     else:
#         print(-1)
#         break

# 3.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

