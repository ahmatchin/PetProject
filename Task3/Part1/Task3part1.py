# 1. Написать программу для поиска наиболее часто встречающихся элементов в строке.
# Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.
#
# Пример:
# Строка:lkseropewdssafsdfafkpwe
# Элементы:3
# 's' встречается 4 раза
# 'e' встречается 3 раза
# 'f' встречается 3 раза

from operator import itemgetter, attrgetter, methodcaller
enter_string = input('Input the string, use the words only, without spacebar: \n')
enter_elements = input('Input the number of elements: \n')
while True:
    if enter_string.isalpha()  == False:
        enter_string = input('Вы ввели цифру(ы) в первом вводе \n''Input the string, use the words only, without spacebar: \n')
    if enter_string.isalpha() == True:
        break
while True:
    if enter_elements.isdigit() == True:
        break
    if enter_elements.isdigit() == False:
        enter_elements = input('Вы ввели букву)\n''Input the number of elements: \n')
enter_elements = int(enter_elements)
result = {i: enter_string.count(i) for i in enter_string}
i = 1
for key in sorted(result, key=result.get, reverse=True):
    if i <= enter_elements:
        print(f'{key} встречается {result[key]}')
    i += 1

