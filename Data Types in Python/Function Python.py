# Создание функций

"""
В Python создание функций является фундаментальным аспектом программирования, позволяющим коду быть более модульным, повторно используемым и читаемым. Функции в Python определяются с помощью
ключевого слова def, за которым следует имя функции и круглые скобки с параметрами
"""

# Объявление функции
def greet():
    print("Hello, world!")

# Вызов функции
greet()  # Hello, world!


# Функция с параметрами
def greet(name):
    print(f"Hello, {name}")

greet("Arslon")
greet("Bob")



# Функция с возвращаемым значением
# Функция может возвращать результат работы с помощью ключевого слова return:
def add(a, b):
    return a + b

result = add(5, 2)
print(result)


# Функции с параметрами по умолчанию
# Если аргумент не передан, используется значение по умолчанию
def greet(name="Guest"):
    print(f"Hello, {name}")

greet() # Hello, Guest!
greet("Arslon") # Hello, Alice!


# Неопределённое количество аргументов
"""
Для передачи произвольного количества аргументов используется *args и **kwargs:

*args — для позиционных аргументов.
**kwargs — для именованных аргументов.
"""

def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)  # Вывод: 1, 2, 3

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(name="Alice", age=25)
# Вывод:
# name = Alice
# age = 25


# Вложенные функции
# Функция может быть определена внутри другой функции
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from inner function!")  # Hello from inner function!


