from matplotlib import pyplot as plt
from collections import defaultdict

with open('students.csv') as file:
    data = file.read().split('\n')

preps = defaultdict(lambda: {str(i): 0 for i in range(2, 11)})
groups = defaultdict(lambda: {str(i): 0 for i in range(2, 11)})

for st in data:
    st = st.split(';')
    preps[st[0]][st[2]] += 1
    groups[st[1]][st[2]] += 1

colors = ['r', 'b', 'y', 'c', 'm', 'darkgreen', 'navy', 'darkslategrey']

"""
# code for preps
for mark in range(3, 11):
    plt.bar(preps.keys(), [preps[prep][str(mark)] for prep in preps.keys()],
            bottom=[sum(list(preps[prep].values())[:(mark-2)]) for prep in preps.keys()],
            color=colors[-mark+3], label=mark)
plt.legend()
plt.title('Marks per preps')
plt.xlabel('Prep')
plt.ylabel('Number of marks')
plt.savefig('preps.png')
"""
# code for groups
for mark in range(3, 11):
    plt.bar(groups.keys(), [groups[group][str(mark)] for group in groups.keys()],
            bottom=[sum(list(groups[group].values())[:(mark-2)]) for group in groups.keys()],
            color=colors[-mark+3], label=mark)
plt.legend()
plt.title('Marks per groups')
plt.xlabel('Group')
plt.ylabel('Number of marks')
plt.savefig('groups.png')

