import matplotlib.pyplot as plt
import numpy as np
from gradient_descent import gradient_descent_fx
from save_plot_data_to_file import save_function_data
from test_data import data_array_fx
def get_fx(x):
 return np.sin(np.pi * x) + x**2

# first plot
x = np.linspace(-6, 6, 2000)  

y = get_fx(x)

for data_entry in data_array_fx:
 data_entry["found_min"] = gradient_descent_fx(data_entry["init_value"], data_entry["learn_rate"], 1000)

save_function_data(1, data_array_fx)

for data_entry in data_array_fx:
 pass
 # print(data_entry["init_value"])
 # print(data_entry["learn_rate"])
 # print(data_entry["min_value"])

start = -2
min_x = gradient_descent_fx(start, 0.005, 1000)
print(min_x)
plt.plot(x, y, label="f(x)")
plt.plot(min_x, get_fx(min_x), marker='o', ls='none', ms=10, label="found min")
plt.plot(start, get_fx(start), marker='*', ls='none', ms=10, label="starting point")
plt.legend(loc="best")
plt.title(r'$f(x)=sin(πx) + x^2$')
plt.xlabel("x")
plt.ylabel("f (x)")
plt.grid()
plt.show()
