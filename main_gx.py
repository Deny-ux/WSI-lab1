import matplotlib.pyplot as plt
import numpy as np
from plot_gx import plot_surface_gx, plot_surface_gx_with_minimum, get_gx
from gradient_descent import gradient_descent_gx
from save_plot_data_to_file import save_function_data
from test_data import data_array_gx


# calculating minimum for testing data
for data_entry in data_array_gx:
 min = gradient_descent_gx(np.array([data_entry["start_x1"], data_entry["start_x2"]]), data_entry["learn_rate"], 1000)
 data_entry["found_min_x1"] = min[0]
 data_entry["found_min_x2"] = min[1]

save_function_data(2, data_array_gx)

# plotting result
x = np.linspace(-50, 50, 500)
y = np.linspace(-30, 30, 500)
X, Y = np.meshgrid(x, y)
Z = get_gx(X, Y)
init_x, init_y = 20, -30
found_minimum = gradient_descent_gx(np.array([init_x, init_y]), 0.005, 1000)

ax = plt.axes(projection="3d")
# plot_surface_gx_with_minimum(ax, -50, 50, 500, -30, 30, 500, init_x, init_y, found_minimum[0], found_minimum[1])

# plot_surface_gx(ax, -50, 50, 500, -30, 30, 500)
plt.show()


