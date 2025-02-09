# Пример создания замыкания:
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure_example = outer_function(10)
print(closure_example(5))

"""
🔹 В этом примере outer_function создает inner_function, которая использует x, переданный в outer_function. Даже после завершения outer_function, внутренняя 
функция все еще имеет доступ к x, что и делает ее замыканием.
"""

# Создание фабрик функций
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

"""
🔹 Здесь multiplier принимает коэффициент factor и возвращает новую функцию multiply, которая умножает переданный ей аргумент на этот коэффициент. 
Таким образом, double всегда умножает число на 2, а triple — на 3.
"""

# Сохранение состояния без глобальных переменных
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter_instance = counter()
print(counter_instance())  # 1
print(counter_instance())  # 2

"""
🔹 В этом примере counter создает переменную count внутри своей области видимости. Внутренняя функция increment использует nonlocal, чтобы изменять count, сохраняя его значение между вызовами функции. 
Таким образом, переменная count остается доступной внутри замыкания даже после выхода из counter.
"""
