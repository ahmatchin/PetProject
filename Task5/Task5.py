def check_str(string_input):
    """ пробегаем по всей строке и возвращаем для указанного Юникод-символа число, представляющее его позицию кода """
    lowercase_letter = []
    uppercase_letter = []
    for i in range(len(string_input)):
        if ord(string_input[i]) in range(65, 91):
            uppercase_letter.append(string_input[i])
        if ord(string_input[i]) in range(97, 123):
            lowercase_letter.append(string_input[i])
    print(f' {len(uppercase_letter)} upper case, ', f' {len(lowercase_letter)} lower case')
    return uppercase_letter, lowercase_letter


check_str('The quick Brow Fox')


def is_prime(num):
    div = 2
    while div * div <= num and num % div != 0:
        div += 1
    return div * div > num


print(is_prime(777))
print(is_prime(787))


def get_ranges(num_list):
    """начинаем итерацию с елемента с индексом 1 и сравниваем с предыдущим, применяем форматированный вывод,
     выполняем проверки на соответствие условиям вывода, если число непарное или единственное то просто выводим его."""
    start = num_list[0]
    for i in range(1, len(num_list)):
        end = num_list[i - 1]
        if num_list[i] - num_list[i - 1] >= 2 and start == end:
            print(f'{end}', end=', ')
            start = num_list[i]
            if i == len(num_list) - 1:
                print(f'{num_list[-1]}')
            continue
        if num_list[i] - num_list[i - 1] >= 2 and i != 1:
            print(f'{start}-{end}', end=', ')
            start = num_list[i]
            end = num_list[i - 1]
            if i == len(num_list) - 1:
                print(f'{num_list[-1]}')
                continue
        if start == end and i == 3:
            i -= 1
            print(f'{start}-{end + 1}')
            start = num_list[i]
            end = num_list[i - 1]
            if i == len(num_list) - 1:
                print(f'{num_list[-1]}')
                continue
        if num_list[i] - num_list[i - 1] == 1 and i == len(num_list) - 1:
            print(f'{start}-{end + 1}')
            start = num_list[i]
            continue
    return


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
get_ranges([1, 2, 3, 4, 5, 6])
