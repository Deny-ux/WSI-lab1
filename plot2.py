import matplotlib.pyplot as plt
from gradient_descent import gradient_descent_gx
import numpy as np
from test_data import data_array_gx
from save_plot_data_to_file import save_function_data

def get_gx(x1, x2):
 return 5 * (np.e **2) - 4*np.e*x1 + x1**2 + 2*np.e*x2 + x2**2

# calculating minimum for testing data
for data_entry in data_array_gx:
 min = gradient_descent_gx(np.array([data_entry["start_x1"], data_entry["start_x2"]]), data_entry["learn_rate"], 1000)
 data_entry["found_min_x1"] = min[0]
 data_entry["found_min_x2"] = min[1]

x = np.linspace(-50, 50, 500)
y = np.linspace(-30, 30, 500)

X, Y = np.meshgrid(x, y)
Z = get_gx(X, Y)
minimum = gradient_descent_gx(np.array([1, 2]), 0.005, 1000)

save_function_data(2, data_array_gx)

ax = plt.axes(projection="3d")

surface = ax.plot_surface(X, Y, Z, cmap="plasma")
ax.set_xlabel('X1-axis')
ax.set_ylabel('X2-axis')
ax.set_zlabel('g(x)')
ax.set_title('3D Surface Plot')
# ax.scatter(minimum[0], minimum[1], get_gx(minimum[0], minimum[1]), color="red", linewidth=4)
plt.colorbar(surface)
plt.show()