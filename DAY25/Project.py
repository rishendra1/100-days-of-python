import pandas as pd

df = pd.read_csv("indian_states_socioeconomic.csv")
print("Total Raw Data: ")
print(df)
df_2011 = df[df.Year == 2011]

df_2011["GDP_per_capita"] = df_2011["GDP_Cr"] * 1e7 / df_2011["Population"]
data = df_2011[["State", "Year", "GDP_Cr", "Population" ,"GDP_per_capita"]]
max_val = data[max(data.GDP_per_capita)]
print(data)
