##############################################
#
# Author: Denys Fokashchuk, 323944 
#
##############################################

import matplotlib.pyplot as plt
import numpy as np
from plot_gx import (plot_surface_gx, plot_surface_gx_with_minimum, get_gx, plot_contour_gx, 
					 plot_contour_gx_with_minimum, plot_contour_gx_with_every_minimum, get_gx)
from gradient_descent import gradient_descent_gx
from save_plot_data_to_file import save_function_data
from test_data import data_array_gx


# calculating minimums for testing data
for data_entry in data_array_gx:
	values = gradient_descent_gx(np.array([data_entry["start_x1"], data_entry["start_x2"]]), data_entry["learn_rate"], 1000)
	min = np.round(gradient_descent_gx(np.array([data_entry["start_x1"], data_entry["start_x2"]]), data_entry["learn_rate"], 1000)[-1], 2)
	data_entry["found_min_x1"] = min[0]
	data_entry["found_min_x2"] = min[1]
	data_entry["g(x)"] = round(get_gx(values[-1][0], values[-1][1]), 2)

# saving found minimums to file result_gx.csv
save_function_data(2, data_array_gx)

# plotting result
x = np.linspace(-50, 50, 500)
y = np.linspace(-30, 30, 500)
X, Y = np.meshgrid(x, y)
Z = get_gx(X, Y)
init_x1, init_x2 = -18, -2*np.e
learn_rate = 0.2
found_minimums = gradient_descent_gx(np.array([init_x1, init_x2]), learn_rate, 1000)
found_minimum = found_minimums[-1]
# plot_contour_gx(X, Y, Z, 20)

# plot_contour_gx_with_minimum(X, Y, Z, 25, init_x1, init_x2, found_minimum[0], found_minimum[1])

plot_contour_gx_with_every_minimum(X, Y, Z, 30, found_minimums, learn_rate)

# ax = plt.axes(projection="3d")
# plot_surface_gx_with_minimum(ax, -50, 50, 500, -30, 30, 500, init_x1, init_x2, found_minimum[0], found_minimum[1], learn_rate)


# plot_surface_gx(ax, -50, 50, 500, -30, 30, 500)


plt.show()


