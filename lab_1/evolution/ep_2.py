import matplotlib.pyplot as plt

points_x = []
points_y = []

with open('frames.txt') as f:
    for j, lines in enumerate(f):
        if not j % 2:
            points_x.append([float(i) for i in lines.split()])
        else:
            points_y.append([float(i) for i in lines.split()])

x_lim = [min([min(i) for i in points_x]), max([max(i) for i in points_x])]
y_lim = [min([min(i) for i in points_y]), max([max(i) for i in points_y])]

fig, axs = plt.subplots(nrows=3, ncols=2)
fig.set_figheight(8)
plt.subplots_adjust(wspace=0.2, hspace=0.3)
coords = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
for coord, x_coord, y_coord in zip(coords, points_x, points_y):
    tmp = axs[coord[0]][coord[1]]

    tmp.plot(x_coord, y_coord)
    tmp.grid()
    tmp.set_title('Frame ' + str(points_y.index(y_coord)))
    tmp.set_xlim([x_lim[0], x_lim[1]])
    tmp.set_ylim([1.1 * y_lim[0], 1.1 * y_lim[1]])
    tmp.set_xticks(range(int(x_lim[0]), int(x_lim[1]), 2))
    tmp.set_yticks(range(int(y_lim[0]), int(y_lim[1]), 2))

plt.savefig('frames.png')