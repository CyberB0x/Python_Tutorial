#Создание кортежа

"""Простой кортеж"""
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Кортеж с разными типами данных
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)

# Одноэлементный кортеж (обязательно запятая!)
single_element = (42,)
print(single_element)


"""Доступ к элементам кортежа"""
my_tuple = (10, 20, 30, 40, 50)

# Доступ по индексу
print(my_tuple[0])  # Первый элемент
print(my_tuple[-1]) # Последний элемент

# Срезы
print(my_tuple[1:4])  # С 1 по 3 элементы

"""Неизменяемость кортежей"""
my_tuple = (1, 2, 3)

# Попытка изменить значение
try:
    my_tuple[0] = 100
except TypeError as e:
    print(f"Ошибка: {e}")


"""Использование кортежей в функциях"""
# Возврат нескольких значений из функции
def get_user_info():
    return "Alice", 30, "Engineer"

name, age, profession = get_user_info()
print(f"Name: {name}, Age: {age}, Profession: {profession}")


"""Вложенный картеж"""
nested_tuple = (1, (10, 50), (2, 3, 4, 5, 6))
print(nested_tuple[1])
print(nested_tuple[1][0])
