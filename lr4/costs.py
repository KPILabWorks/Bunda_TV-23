import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Вихідні дані
hours = 24
total_energy = 1000  # Загальне енергоспоживання за добу (в кВт·год)

# Тариф на електроенергію по годинах (наприклад, пікові години — дорожче)
tariffs = np.array([
    1.2, 1.1, 1.0, 0.9, 0.8, 0.7,  # ніч — дешевше
    1.0, 1.5, 2.0, 2.2, 2.5, 2.3,  # день — дорожче
    2.1, 2.0, 1.9, 1.7, 1.6, 1.5,
    1.3, 1.2, 1.1, 1.0, 0.9, 0.8   # вечір — середнє
])

# Цільова функція: мінімізувати сумарну вартість електроенергії
def cost(x):
    return np.sum(x * tariffs)

# Обмеження: загальне споживання має дорівнювати total_energy
cons = {'type': 'eq', 'fun': lambda x: np.sum(x) - total_energy}

# Межі для кожної години: від 0 до 100 кВт·год (наприклад)
bounds = [(0, 100) for _ in range(hours)]

# Початкове наближення — рівномірний розподіл
x0 = np.full(hours, total_energy / hours)

# Оптимізація
result = minimize(cost, x0, method='SLSQP', bounds=bounds, constraints=cons)

# Результат
optimized_load = result.x
optimized_cost = cost(optimized_load)

# Евристичний варіант — рівномірний розподіл
heuristic_load = x0
heuristic_cost = cost(heuristic_load)

# Вивід результатів
print(f"Оптимізована вартість: {optimized_cost:.2f} грн")
print(f"Евристична вартість: {heuristic_cost:.2f} грн")

# Побудова графіків
plt.figure(figsize=(12, 6))
plt.plot(range(24), heuristic_load, label='Евристика (рівномірно)', linestyle='--')
plt.plot(range(24), optimized_load, label='Оптимізовано (SciPy)', linewidth=2)
plt.xticks(range(24))
plt.xlabel('Година доби')
plt.ylabel('Подача енергії (кВт·год)')
plt.title('Порівняння графіків навантаження')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
