import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Dirichlet kernel function
def dirichlet_kernel(x, N):
    return np.sin((N + 0.5) * x) / np.sin(0.5 * x)

# x range and initial N
x = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
N = 1

# Plot setup
fig, ax = plt.subplots()
line, = ax.plot(x, dirichlet_kernel(x, N), lw=2)
ax.set_ylim([-5, 10])  # Fix y-axis range

# Update function
def update(N):
    y = dirichlet_kernel(x, N)
    line.set_ydata(y)
    ax.set_title(f"Dirichlet Kernel, N = {N}")
    return line,

# Animation settings
ani = FuncAnimation(fig, update, frames=np.arange(1, 50), interval=200, blit=True)

# Show plot
plt.show()
