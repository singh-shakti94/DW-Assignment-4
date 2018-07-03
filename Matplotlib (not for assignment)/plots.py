import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

C,S = np.cos(X), np.sin(X)

# line plot
plt.plot(X, C)
plt.plot(X, S)
plt.show()

# scatter plot
n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=0.5)

plt.xlim(-1.5, 1.5)
plt.xticks([])
plt.ylim(-1.5, 0.5)
plt.yticks([])
plt.show()


# 3D plot
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
ax.contour(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
ax.set_zlim(-2,2)
plt.show()


# Subplots
from pylab import *

subplot(2, 1, 1)
xticks([])
yticks([])
text(0.5, 0.5, "Subplot(2,1,1)", ha="center", va="center", size=24, alpha=0.5)

subplot(2, 1, 2)
xticks([])
yticks([])
text(0.5, 0.5, "Subplot(2,1,2)", ha="center", va="center", size=24, alpha=0.5)

show()


# more subplots
subplot(1, 2, 1)
xticks([])
yticks([])
text(0.5, 0.5, "Subplot(1,2,1)", ha="center", va="center", size=12, alpha=0.5)

subplot(1, 2, 2)
xticks([])
yticks([])
text(0.5, 0.5, "Subplot(1,2,2)", ha="center", va="center", size=12, alpha=0.5)

show()


# Subplots with axes
import matplotlib.gridspec as gridspec

G = gridspec.GridSpec(3, 3)

axes_1 = subplot(G[0, :])
xticks([])
yticks([])
text(0.5, 0.5, "Axes 1", ha="center", va="center", size=12, alpha=0.5)

axes_2 = subplot(G[1, :-1])
xticks([])
yticks([])
text(0.5, 0.5, "Axes 2", ha="center", va="center", size=12, alpha=0.5)

axes_3 = subplot(G[1:, -1])
xticks([])
yticks([])
text(0.5, 0.5, "Axes 3", ha="center", va="center", size=12, alpha=0.5)

axes_4 = subplot(G[-1, 0])
xticks([])
yticks([])
text(0.5, 0.5, "Axes 4", ha="center", va="center", size=12, alpha=0.5)

axes_5 = subplot(G[-1, -2])
xticks([])
yticks([])
text(0.5, 0.5, "Axes 5", ha="center", va="center", size=12, alpha=0.5)

show()