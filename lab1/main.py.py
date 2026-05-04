from datetime import datetime
# 1 Программа запрашивает
# Имя (str)
# Фамилия (str)
# Год рождения (int)
# Рост в сантиметрах (float)

# 2 Вычислить возрасть
# 3 Вывод в виде рамки из символов


# Считает сегодняшний год
now = datetime.now()
now_year = now.year


print("********************\n*  Личная Визитка  *\n********************")

# Запросы
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
birth_year = int(input("Введите год рождения: "))
height = float(input("Введите ваш рост: "))

print("********************\n*   Ваша Визитка   *\n********************")

# Вывод
print(f"Имя: {name} \nФамилия: {surname} \nГод рождкеия: {birth_year} \nВозраст: {now_year - birth_year} \nРост: {height}")
