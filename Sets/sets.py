# Создание множества
# Создание множества с использованием фигурных скобок
my_set = {1, 2, 3, 4, 5}
print(my_set)


# Добавление элемента в множество:
my_set.add(6)
print(my_set)

# Удаление элемента из множества
my_set.remove(4)
print(my_set)

# Объединение двух множеств
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)

# Пересечение двух множеств
intersection_set = set1 & set2
print(intersection_set)

# Разность множеств
difference_set = set1 - set2
print(difference_set)

# Проверка наличия элемента в множестве
print(2 in my_set)
print(7 in my_set)

