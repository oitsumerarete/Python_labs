import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("flights.csv")

df.drop(df.columns[0], axis=1)

CARGO = list(set(df.CARGO))
PRICE = []
WEIGHT = []
FLIGHTS = []

for company in CARGO:
    PRICE.append(df.loc[df.CARGO == company].PRICE.sum())
    WEIGHT.append(df.loc[df.CARGO == company].WEIGHT.sum())
    FLIGHTS.append(df.loc[df.CARGO == company].shape[0])

fig, axs = plt.subplots(ncols=3)
axs[0].set_title('Number of flights')
axs[1].set_title('Total value of goods transported')
axs[2].set_title('Total mass transported')
fig.set_figwidth(10)
plt.subplots_adjust(wspace=0.5)

for company in CARGO:
    print(str(company), ": ", len(df.loc[df.CARGO == company].CARGO))
    number_of_flights = len(df.loc[df.CARGO == company].CARGO)
axs[0].bar(CARGO, WEIGHT, color='red')
axs[1].bar(CARGO, PRICE, color='royalblue')
axs[2].bar(CARGO, FLIGHTS, color='magenta')
plt.savefig('episode_2.png')






