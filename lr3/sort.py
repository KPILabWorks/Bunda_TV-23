import numpy as np
import time
from numba import njit
import matplotlib.pyplot as plt

# Генеруємо великі масиви даних для генерації та споживання енергії
np.random.seed(0)
data_generation = np.random.rand(10_000_000) * 1000  # генерація в МВт
data_consumption = np.random.rand(10_000_000) * 1000  # споживання в МВт

# Сортування з NumPy
start_np = time.time()
sorted_generation_np = np.sort(data_generation)
end_np = time.time()
numpy_sort_time = end_np - start_np
print(f"NumPy сортування зайняло: {numpy_sort_time:.4f} секунд")

# Сортування
@njit
def numba_sort(arr):
    # Просте сортування методом вставки (для прикладу, підходить лише для демонстрації)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Щоб не змінити оригінальні дані:
data_copy = data_generation[:10000].copy()  # сортуємо менший масив, бо вставка повільна

start_numba = time.time()
sorted_generation_numba = numba_sort(data_copy)
end_numba = time.time()
numba_sort_time = end_numba - start_numba
print(f"Numba сортування (на 10 тис. елементах) зайняло: {numba_sort_time:.4f} секунд")

methods = ['NumPy (10 млн)', 'Numba (10 тис)']
times = [numpy_sort_time, numba_sort_time]

plt.bar(methods, times, color=['blue', 'orange'])
plt.ylabel('Час сортування (секунди)')
plt.title('Порівняння швидкості сортування NumPy vs Numba')
plt.show()