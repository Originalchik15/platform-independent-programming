# 1: Меню. 1- создать заметку 2- показать все заметки 3- найти заметку по дате 4- выход
# 2: Создание - 1. Запрос заголовка 2. Запрос текста 3. Авто добавление текущей даты и времени 4. Сохранить в json 
# 3: Просмотр - 1. Прочитать json 2. Вывести все заметки красиво 3. Показать кол-во заметок
# 4: Поиск по дате - 1. Запрос даты ДД.ММ.ГГГ 2. Показать все заметки в этот день
# 5: pathlib, datetime, json

import json
import pathlib
from datetime import datetime

folder = pathlib.Path('json')
folder.mkdir(parents=True, exist_ok=True)
filename = "profile.json"
path_obj = pathlib.Path(folder / filename)

def create_note():
    headline = input("| Введите название заголовка: ")
    text = input("| Введите текст: ")
    date_now = datetime.now().strftime("%d-%m-%Y")
    note = {
        "Заголовок": headline,
        "Текст": text,
        "Дата": date_now
    }


    #Записать весь json в data
    with open(path_obj, 'r',encoding="utf-8") as f:
            data = json.load(f)

    #Добавить в data новую заметку
    data.append(note)

    #Залить обратно в json
    with open(path_obj, 'w',encoding="utf-8") as f:
        json.dump(data, f, indent= 4 ,ensure_ascii=False)
        



def read_note():
    with open(path_obj, "r", encoding="utf-8") as f:
        data = json.load(f)
    #Содержимое json
    print('+-----------------------------------------------+')
    print('|  Заголовок   |        Текст        |   Дата   |')
    print('+-----------------------------------------------+')
    for s in data:
        print('|  ',s["Заголовок"],'   ', s["Текст"],'     ', s["Дата"],'  ')
    #Кол-во заметок
    print(f"|----Количество заметок: ({len(data)})----|\n")

def find_by_date(date):
    print('+-----------------------------------------------+')
    print('|  Заголовок   |        Текст        |   Дата   |')
    print('+-----------------------------------------------+')
    cnt = 0
    with open(path_obj, "r", encoding="utf-8") as f:
        data = json.load(f)
    for s in data:
         if date == s["Дата"]:
               cnt+=1
               print('|  ',s["Заголовок"],'   ', s["Текст"],'     ', s["Дата"],'  ')
    print('\n')
    if cnt == 0:
        print('| Похоже в эту дату заметки отсутствуют\n')

choose = 0

while choose != 4:
    try:
        choose = int(input(
        "+----------Меню-----------+" \
    "\n|1. Создать заметку       | " \
    "\n|2. Прочитать все заметки | " \
    "\n|3. Поиск заметок по дате | " \
    "\n|4. Выход                 |" \
    "\n+-------------------------+ " \
    "\nВаш выбор: "))
    except:
        print('Неверный выбор\n')
        choose = 0
        continue

    if choose == 1:
        create_note()
    elif choose == 2:
        read_note()
    elif choose == 3:
        check = False
        while not check:
            date_input = input("Введите дату (ДД-ММ-ГГГГ): ")
            try:
                datetime.strptime(date_input.strip(), '%d-%m-%Y')
                check = True
            except:
                print('Неверный формат даты\n')

        find_by_date(date_input)
    elif choose == 4:
        print('Выходим')
    else:
        print('Неверный выбор\n')
