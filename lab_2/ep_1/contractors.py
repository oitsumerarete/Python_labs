import pandas as pd

df = pd.read_csv("transactions.csv")
df.drop(df.columns[0], axis=1)

print("3 most expensive payments: ")
print(df.loc[df.STATUS == 'OK'].SUM.sort_values()[-3:])

print("\n Umbrella, Inc summary income: ")
print(df.loc[(df.STATUS == 'OK') & (df.CONTRACTOR == 'Umbrella, Inc')].SUM.sum())