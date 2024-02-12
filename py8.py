
import os


INFO_STRING = """ 
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
"""


DATASOURCE = 'phone.txt'


def check_directory(filename: str):
    if filename not in os.listdir():
        with open(filename, 'w', encoding = 'utf-8') as data:
            data.write("")


check_directory(DATASOURCE)


def add_new_user(name: str, phone: str, filename: str):
    with open(filename, 'r+t', encoding='utf-8') as wrtbl:
       lins_count = len(wrtbl.readlines())
       wrtbl.write(f"{lins_count + 1};{name};{phone}\n")


def read_all(filename: str) -> str:
    with open(filename, 'r', encoding = 'utf-8') as data:
        result = data.read()   
    return result


def search_user(search_pattern: str, filename: str) -> str:
    with open(filename, 'r+t', encoding = 'utf-8') as data:
        phonebook = data.readlines()
        for line in phonebook:
            row_num, name, num = tuple(line.split(';'))
            if search_pattern in name or search_pattern in num:
                print(line)


while True:
    mode = 3#int(input(INFO_STRING))
    if mode == 1:        
        print(read_all(DATASOURCE))
    elif mode == 2:
        user = input()
        phone = input()
        add_new_user(name=user, phone=phone, filename=DATASOURCE)
    elif mode == 3:
        search_user(input("Имя или номер: "), DATASOURCE)