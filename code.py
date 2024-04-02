import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    if read_all(filename) != '':
        with open(filename, 'a', encoding="utf-8") as file:
            file.write(f"\n{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open("number.txt", 'r', encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        list_1 = file.read().split('\n')
    result = []
    for i in list_1:
        if data in i:
            result.append(i)
    if not result:
        return "Совпадений нет"
    return '\n'.join(result)


def transfer_data(source: str, dest: str, num_row: int):
    """
    Перенос записи в другой файл.
    """


with open("number.txt", 'r', encoding="utf-8") as firstfile, open("new_number.txt", 'w', encoding="utf-8") as secondfile:
    for num_row in firstfile:
        secondfile.write(num_row)


INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
"""
file = "number.txt"
if file not in os.listdir():
    print("Такого файла не существует")
    sys.exit()
new_file = "new_number.txt"
num_row

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
    elif mode == 2:
        name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("Введите значение для поиска: ")
        print(search_user(file, data))
    elif mode == 4:
        num_row = int(input("Введите номер строки для переноса в new_number.txt: "))
        print("Готово, откройте файл 'new_number.txt' и проверьте")