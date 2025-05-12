import pandas as pd

df = pd.read_csv("World-happiness-report-2024.csv")
print(df[df["Healthy life expectancy"] > 0.7])