import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("flights.csv", index_col=0)
df.reset_index()

newdata = df.groupby('CARGO').sum()
newdata['COUNTS'] = df.groupby('CARGO').count()['PRICE'].values
fig, axs = plt.subplots(ncols=3)

for i in newdata.columns:
    newdata[i].plot.bar(ax=axs[list(newdata.columns).index(i)],
                        fontsize=12, figsize=(10, 8), title=i, color=['c', 'm', 'royalblue'])
    axs[list(newdata.columns).index(i)].title.set_size(15)
fig.tight_layout(pad=1.0)
plt.savefig('episode_2.png')






