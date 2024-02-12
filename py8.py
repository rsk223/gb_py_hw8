
import os


INFO_STRING = """ 
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - копирование в другую книжку
5 - выход
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
        result = data.readlines()
        result = [tuple(line.split(';')) for line in result]
        result = [f"{l[0]}. {l[1]}: {l[2]}" for l in result]
        result = "".join(result)
    return result


def search_user(filename: str, search_pattern: str=None, row=0) -> tuple:
    with open(filename, 'r', encoding = 'utf-8') as data:
        phonebook = data.readlines()
        for line in phonebook:
            row_num, name, num = tuple(line.split(';'))
            if row != 0:
                if int(row_num) == row:
                    yield row_num, name, num
            elif search_pattern is not None:
                if search_pattern in name or search_pattern in num:
                    yield row_num, name, num
            else:
                return None


def copy_to_another(copy_to: str, rnum: str):
    check_directory(copy_to)
    val = search_user(filename=DATASOURCE, row=rnum)
    val = list(val)
    if len(val) == 1:
        val = val[0]
        row_num, name, num = val
        add_new_user(name.strip(), num.strip(), copy_to)
    else:
        print("В искомом словаре такой записи нет или в словаре больше одной с таким номером")


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:        
        print(read_all(DATASOURCE))
    elif mode == 2:
        user = input("Имя: ")
        phone = input("Номер: ")
        add_new_user(name=user, phone=phone, filename=DATASOURCE)
    elif mode == 3:
        res = search_user(filename=DATASOURCE, search_pattern=input("Имя или номер: "))
        #res = list(res)
        for r in res:
            row_num, name, num = r
            print(f"{row_num.strip()}. {name.strip()}: {num.strip()}")      
    elif mode == 4:
        copyname = input("Имя файла: ")
        row_num = int(input("Номер записи для копии: "))
        copy_to_another(copy_to=copyname, rnum=row_num)
    elif mode == 5:
        break