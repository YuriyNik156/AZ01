# 1. Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# * Загрузите набор данных из CSV-файла в DataFrame.
# * Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# * Выведите информацию о данных (.info()) и статистическое описание (.describe()).

import pandas as pd

df = pd.read_csv("Greenhouse Plant Growth Metrics.csv") # Загрузка набора данных из CSV в DataFrame

print(df.head()) # Вывод первых пяти строк данных

print(df.info()) # Вывод информации о данных

print(df.describe()) # Статистическое описание данных
