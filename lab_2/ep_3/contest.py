import pandas as pd
from matplotlib import pyplot as plt

df1 = pd.read_html("results_ejudge.html")[0]
df2 = pd.read_excel('students_info.xlsx')

df1.fillna(0, inplace=True)
df2.dropna(inplace=True)

newdata = df1.merge(df2, how='inner', left_on="User", right_on="login")
faculty_groups = newdata.groupby(['group_faculty']).Solved.mean().index
average_per_faculty_groups = newdata.groupby(['group_faculty']).Solved.mean().values

groups_out = newdata.groupby(['group_out']).Solved.mean().index
average_per_groups_out = newdata.groupby(['group_out']).Solved.mean().values

fig, axs = plt.subplots(1, 2)
axs[0].set_title('Average of solved problems by faculty groups')
axs[1].set_title('Average of solved problems by informatics groups')
fig.set_figwidth(11)
plt.subplots_adjust(wspace=0.2)

axs[0].bar(list(map(str, faculty_groups)), average_per_faculty_groups)
axs[0].set_xlabel('faculty_group')
axs[0].set_ylabel('average mark')

axs[1].bar(list(map(str, groups_out)), average_per_groups_out)
axs[1].set_xlabel('group_out')

plt.savefig('average_marks.png')
print("Номера факультетских групп: ", set(newdata.loc[(df1.H > 10) | (df1.G > 10)].group_faculty))
print("Номера групп по информатике: ", set(newdata.loc[(df1.H > 10) | (df1.G > 10)].group_out))