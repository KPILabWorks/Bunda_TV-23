import time
from functools import wraps

def rate_limited(max_calls=1, period=2):
    """
    Декоратор, що обмежує частоту виклику функції.

    :param max_calls: Максимальна кількість викликів, що допускаються за період.
    :param period: Період у секундах, протягом якого допускаються виклики.
    """
    def decorator(func):
        last_called = [0.0]  # Список для зберігання останнього часу виклику

        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] >= period:
                # Якщо пройшов достатній період з останнього виклику
                result = func(*args, **kwargs)
                last_called[0] = time.time()  # Оновлюємо час останнього виклику
                return result
            else:
                # Якщо ще не минув період, повертаємо None або виконуємо іншу обробку
                print(f"Функція {func.__name__} обмежена частотою викликів. Зачекайте ще трохи.")
                return None  # Можна викинути виняток, залежно від потреб

        return wrapper

    return decorator

# Приклад використання декоратора
@rate_limited(max_calls=1, period=2)
def hello():
    print("Hello, world!")

# Тестуємо функцію
hello()  # Викличемо один раз
time.sleep(1)  # Почекаємо 1 секунду
hello()  # Цей виклик буде заблокований
time.sleep(2)  # Почекаємо 2 секунди
hello()  # Цей виклик буде допущений
