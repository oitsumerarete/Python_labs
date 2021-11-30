import matplotlib.pyplot as plt
print("Введите имя нужного файла с данными:")
filename = input()
points_x = []
points_y = []
with open(filename, 'r') as f:
    lines = f.readlines()
    N = int(lines[0])
    for text in lines[1:N + 1]:
        x, y = (text.split())
        x = float(x)
        y = float(y)
        points_x.append(x)
        points_y.append(y)

if len(points_x) > 100:
    points_size = 2
else:
    points_size = 5
plt.plot(points_x, points_y, '.', markersize=points_size)
plt.axis('equal')
plt.axis('scaled')
plt.title("Number of points: " + str(N))
print("Имя сохраненного графика:")
save = input()
plt.savefig(save)
plt.show()
