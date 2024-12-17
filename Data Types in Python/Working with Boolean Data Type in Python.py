# Работа с логическим типом

"""
В Python логический тип (bool) имеет два значения: True и False. Это основные типы данных, которые используются для работы с логическими выражениями и операциями.
Вот несколько примеров работы с логическим типом
"""
# Создание переменных логического типа
is_active = True
is_logged_in = False
print(is_active)  # True
print(is_logged_in)  # False


# Операции сравнения
a = 10
b = 20
print(a > b)  # False
print(a < b)  # True
print(a == b)  # False
print(a != b)  # True

# Логические операторы
"""
and — логическое "И" (True, если оба значения True).
or — логическое "ИЛИ" (True, если хотя бы одно значение True).
not — логическое "НЕ" (инвертирует значение).
"""
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False


# Использование в условных конструкциях
is_admin = True

if is_admin:
    print("Welcome, admin!")
else:
    print("Access denied.")


# Преобразование типов
"""
Логические значения можно преобразовывать в другие типы.
Любое значение в Python имеет "логическую истину":
Значения, которые считаются ложными: 0, None, пустые структуры данных ([], {}, '').
Все остальные значения считаются истинными.
"""
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Python")) # True


# Логические выражения с циклами
count = 0
is_running = True

while is_running:
    print(count)
    count += 1
    if count > 5:
        is_running = False


# Функции, возвращающие логическое значение
text = "Python"
print(text.isalpha())  # True (если строка состоит только из букв)
print(text.isdigit())  # False (если строка содержит только цифры)



