import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = np.loadtxt('start.dat')
A = np.diag(np.ones(data.size), 0)
A[np.arange(data.shape[0]), np.arange(data.shape[0])-1] = -1
fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(0, 10))
line, = ax.plot([], [])
plt.grid()


def init():
    line.set_data([], [])
    return line,


def update(i):
    global data
    plt.title('Process time step: ' + str(i))
    if not i:
        line.set_data(np.linspace(0, 50, 50), data)
    else:
        data -= 0.5 * A.dot(data)
        line.set_data(np.linspace(0, 50, 50), data)
    return line,


anim = FuncAnimation(fig, update, init_func=init, frames=255, interval=100, blit=True)
anim.save('result.gif', writer='pillow')