# Пример простой лямбда-функции:
square = lambda x: x ** 2
print(square(5))

"""
Использование лямбда-функций
Лямбда-функции часто используются с функциями map(), filter() и sorted().
"""
# Пример с map() , который применяет функцию ко всем элементам списка:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Пример с filter(), который оставляет только четные числа:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Пример с sorted(), который сортирует список по последнему символу строки:
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: x[-1])
print(sorted_words)