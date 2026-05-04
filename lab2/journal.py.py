# 1 Добавить новую запись, показать все записи ,очистить журнал, выход 
# 2 Добавление - Запросить дату ГГГГ-ММ-ДД с проверкой корректности, Оценку от 1 до 10 с проверкой, Сохранить файл в формате Дата | Оценка | Текст
# 3 Просмотр всех записей - Прочитать файл и вывести все записи в красивой таблице, Вывести статистику: кол-во записей и ср. оценку
# 4 Очистка журнала - удалить содержимое или сам файл и создать новый
# 5 Все пути к файлам формироваться через pathlib, файл с данными в папке data, создаётся сама
import pathlib
from datetime import datetime

#Создание директории если нет
folder = pathlib.Path('data')
folder.mkdir(parents=True, exist_ok=True)

#функция создания txt с именем записи
def make_txt(date_input, rating, text):
    content = (f'|{date_input} |   {rating}    | {text} |')
    filename = content + ".txt"
    path_obj = pathlib.Path(folder / filename)
    path_obj.touch()

# Запрос у пользователя данных
def new_entry():
    check = False
    while not check:
        date_input = input("Введите дату (ГГГГ-ММ-ДД): ")
        try:
            datetime.strptime(date_input.strip(), '%Y-%m-%d')
            check = True
        except:
            print('Неверный формат даты')

    text = input("Введите текст наблюдения: ")
    check = False
    while not check: 
        rating = int(input("Введите оценку (1-10): "))
        if rating >= 1 and rating <= 10:
            check = True
        else:
            print("Неверная оценка")
    
    make_txt(date_input,rating,text)

#Чтение имён файлов
def read_files():
    print("---Все записи---")
    print("+----------+--------+---------------+")
    print("|   Дата   | Оценка |     Текст     |")
    print("+----------+--------+---------------+")

    all_rates = []
    for file in folder.glob('*.txt'):
        filename = file.stem
        print(filename)
        rate = filename.split()
        all_rates.append(int(rate[2])) 
    #print(all_rates)
    print("+----------+--------+---------------+\n")
    print("Статистика: ")
    print(f"Всего записей: {len(all_rates)}")
    print(f"Средняя оценка: {(sum(all_rates) / len(all_rates))}")

#Поиск всех txt их удаление
def delete_files():
    for file in folder.glob('*.txt'):
        file.unlink()
    print("Все записи удалены")

while True:
    print("========================= \n Журнал Наблюдений \n=========================")
    print("Выберете действие \n1. Добавить запись \n2. Показать все записи \n3. Очистить журнал \n4. Выход")
    choose = int(input("Ваш выбор: "))
    if choose == 1:
        print("---Добавление новой записи---")
        new_entry()
        print("Запись добавлена")
    elif choose == 2:
        read_files()
    elif choose == 3:
        delete_files()
    elif choose == 4:
        print("Выходим")
        break
    else:
        print("Неверный выбор")