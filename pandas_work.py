import pandas as pd

df = pd.read_csv("hh.csv", sep = ";")


df.drop(49, axis = 0, inplace = True)

print(df)

df.to_csv("output.csv", index = False)