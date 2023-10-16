import matplotlib.pyplot as plt
import numpy as np
from test_data import data_array_fx
from gradient_descent import gradient_descent_fx
from save_plot_data_to_file import save_function_data
from plot_fx import get_fx, plot_fx, plot_fx_with_minimum



for data_entry in data_array_fx:
 data_entry["found_min"] = gradient_descent_fx(data_entry["init_value"], data_entry["learn_rate"], 1000)

save_function_data(1, data_array_fx)

# init_x = 5
# min_x = gradient_descent_fx(init_x, 0.01)

# plot_fx(-5, 5, 500)
# plot_fx_with_minimum(-5, 5, 500, init_x, min_x)
# plt.show()
