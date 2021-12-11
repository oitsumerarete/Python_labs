import pandas as pd
from matplotlib import pyplot as plt

df1 = pd.read_html("results_ejudge.html")[0]
df2 = pd.read_excel('students_info.xlsx')

df1.fillna(0, inplace=True)
df2.dropna(inplace=True)

newdata = df1.merge(df2, how='inner', left_on="User", right_on="login")

fig, axs = plt.subplots(1, 2)
axs[0].set_title('Average of solved problems by faculty groups')
axs[1].set_title('Average of solved problems by informatics groups')
fig.set_figwidth(11)
plt.subplots_adjust(wspace=0.2)

newdata[['group_faculty', 'Solved']].groupby('group_faculty').mean().plot(kind='bar', color='m', rot=0, ax=axs[0],
                                                                          title='per faculty groups', legend=False)
newdata[['group_out', 'Solved']].groupby('group_out').mean().plot(kind='bar', color='royalblue', rot=0, ax=axs[1],
                                                                  title='per out groups', legend=False)

plt.savefig('average_marks.png')
print("Номера факультетских групп: ", set(newdata.loc[(df1.H > 10) | (df1.G > 10)].group_faculty))
print("Номера групп по информатике: ", set(newdata.loc[(df1.H > 10) | (df1.G > 10)].group_out))