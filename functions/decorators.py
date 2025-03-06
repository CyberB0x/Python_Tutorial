# Логирование выполнения функции
import time

# Декоратор логирования
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"[{time.strftime('%H:%M:%S')}] Вызов функции {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Привет, мир!")

say_hello()


# Кеширование результатов в вычислениях
import time
from functools import lru_cache

# Декоратор кеширования
@lru_cache(maxsize=5)
def expensive_function(x):
    time.sleep(2)  # Симуляция долгого вычисления
    return x * x

print(expensive_function(4))  # Долго считает
print(expensive_function(4))  # Быстро из кеша



# Ограничение доступа по ролям
from functools import wraps

# Фейковый пользователь
current_user = {"role":"admin"}

# Декоратор проверки доступа
def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.get("role") != "admin":
            return "Доступ запрещен!"
        return func(*args, **kwargs)
    return wrapper

@require_admin
def del_user():
    return "Пользователь удалён"

print(del_user()) # Доступ запрещён