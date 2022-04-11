# -*- coding: utf8 -*-
while True:
    user_enter = input("Enter max value of symbols in string > or = 36: \n")
    if not user_enter.isdigit():
        print("Did you read conditions!")
        continue
    user_enter = int(user_enter)
    if user_enter < 36:
        print("Did you read conditions?\n")
        continue
    break
# открываем, читам, разбиваем на слова строки и слова
with open("text.txt", "r", encoding='utf-8') as f, open('edit_text.txt', 'w', encoding='utf-8') as edit_text:
    width = 0
    line = []
    for text in f:                       # бьем на строки
        text = text.split()              # бьем на слова
        for words in text:               # помещаем в список добавляя слова + пробелы, измеряем длину строки
            if width + len(words) < user_enter:
                line.append(words), line.append(" ")
                width += len(words) + 1
            else:                                        # удаляем последний пробел изменяем длину строки
                del line[-1]
                width -= 1
                while width != user_enter:                # в цикле добавлем пробелы которых не достает
                    for index, value in enumerate(line):  # до нужной длины строки, убираем пробел в конце
                        if line[-1] == ' ':
                            del line[-1]
                            width -= 1
                        if width == user_enter:
                            break
                        if value != " ":
                            line.insert(index + 1, " ")
                            width += +1
                if width == user_enter:                   # форматированный результат пишем в файл,
                    print("".join(line), file=edit_text)  # переходим к следующей итерации
                    line = [words, " "]
                    width = len(words) + 1
        print("".join(line), file=edit_text)
        line = []
        width = 0
print("The edited text is in the file: 'edit_text.txt' ")
