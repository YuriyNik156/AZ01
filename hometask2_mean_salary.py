# 2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

import pandas as pd

df = pd.read_csv("dz.csv") # Загрузка набора данных из CSV в DataFrame

df.fillna(value = 0, inplace = True) # Замена пустых значений на 0.0

group = df.groupby("City")["Salary"].mean() # Вывод средней зарплаты по городам

print(group)
