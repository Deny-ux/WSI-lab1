##############################################
#
# Author: Denys Fokashchuk, 323944 
#
##############################################

import matplotlib.pyplot as plt
from test_data import data_array_fx
from gradient_descent import gradient_descent_fx
from save_plot_data_to_file import save_function_data
from plot_fx import plot_fx, plot_fx_with_minimum, plot_fx_with_every_minimum, get_fx



for data_entry in data_array_fx:
 values = gradient_descent_fx(data_entry["init_value"], data_entry["learn_rate"], 5000)
 data_entry["found_min"] = round(values[-1], 2)
 data_entry["f(x)"] = round(get_fx(values[-1]), 2)

save_function_data(1, data_array_fx)

init_x = 2
learn_rate = 0.1
values = gradient_descent_fx(init_x, learn_rate)

# plot_fx(-5, 5, 500)
plot_fx_with_every_minimum(-5, 5, 500, values, learn_rate)
# plot_fx_with_minimum(-5, 5, 500, init_x, learn_rate, values[-1])
plt.show()
