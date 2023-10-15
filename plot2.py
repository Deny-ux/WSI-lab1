import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from get_gradient import get_gradient_gx
from gradient_descent import gradient_descent_gx
import numpy as np

def get_gx(x1, x2):
 return 5 * (np.e **2) - 4*np.e*x1 + x1**2 + 2*np.e*x2 + x2**2


x = np.linspace(-50, 50, 500)
y = np.linspace(-30, 30, 500)

X, Y = np.meshgrid(x, y)
minimum = gradient_descent_gx(np.array([1, 2]), 0.005, 1000)
Z = get_gx(X, Y)
#################
fig = plt.figure()

ax = plt.axes(projection="3d")

surface = ax.plot_surface(X, Y, Z, cmap="plasma")
ax.set_xlabel('X1-axis')
ax.set_ylabel('X2-axis')
ax.set_zlabel('g(x)')
ax.set_title('3D Surface Plot')
# ax.scatter(minimum[0], minimum[1], get_gx(minimum[0], minimum[1]), color="red", linewidth=4)
plt.colorbar(surface)
plt.show()


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# a = gradient_descent_gx(np.array([1, 2]), 0.01, 1000)
# surface = ax.plot_surface(X, Y, Z, cmap='viridis')

# ax.set_xlabel('X1-axis')
# ax.set_ylabel('X2-axis')
# ax.set_zlabel('g(x)')
# ax.set_title('3D Surface Plot')

# fig.colorbar(surface)

# plt.show()

#################
###
##scatter
# ax = plt.axes(projection="3d")
# ax.scatter(3, 5, 7)
###
##scatter
# ax = plt.axes(projection="3d")
# x_data = np.random.randint(0, 100, (500,))
# y_data = np.random.randint(0, 100, (500,))
# z_data = np.random.randint(0, 100, (500,))
# ax.scatter(x_data,y_data,z_data)
###
##line charts 3d
# ax = plt.axes(projection="3d")
# x_data = np.arange(0, 50, 0.1)
# y_data = np.arange(0, 50, 0.1)
# z_data = x_data * y_data
# ax.plot(x_data,y_data,z_data)
###
## surface

# ax = plt.axes(projection="3d")

# x_data = np.arange(0, 50, 0.1)
# y_data = np.arange(0, 50, 0.1)

# X, Y = np.meshgrid(x_data, y_data)
# Z = X * Y


# ax.plot_surface(X, Y, Z, cmap="plasma")
# ax.view_init(azim=0, elev=90)
# plt.show()



