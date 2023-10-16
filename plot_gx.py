import matplotlib.pyplot as plt
from gradient_descent import gradient_descent_gx
import numpy as np
from test_data import data_array_gx
from save_plot_data_to_file import save_function_data
from typing import Union

def get_gx(x1: Union[int, float], x2: Union[int, float]):
 """
 Get the value of function g(x) in point x1, x2
 """
 return 5 * (np.e **2) - 4*np.e*x1 + x1**2 + 2*np.e*x2 + x2**2

def plot_surface_gx(axes, start_x: Union[int, float], end_x: Union[int, float], number_point_x: int, start_y: Union[int, float], end_y: Union[int, float], number_point_y: int):
 x = np.linspace(start_x, end_x, number_point_x)
 y = np.linspace(start_y, end_y, number_point_y)
 X, Y = np.meshgrid(x, y)
 Z = get_gx(X, Y)
 # ax = plt.axes(projection="3d")
 surface = axes.plot_surface(X, Y, Z, cmap="plasma")
 axes.set_xlabel('X1-axis')
 axes.set_ylabel('X2-axis')
 axes.set_zlabel('g(x)')
 axes.set_title('3D Surface Plot')
 plt.colorbar(surface)

def plot_surface_gx_with_minimum(axes, start_x: Union[int, float], end_x: Union[int, float], number_point_x: int, start_y: Union[int, float], end_y: Union[int, float], number_point_y: int, init_x1:Union[int, float], init_x2: Union[int, float], min_x1: Union[int, float], min_x2: Union[int, float]):
 plot_surface_gx(axes, start_x, end_x, number_point_x, start_y, end_y, number_point_y)
 min_z = get_gx(min_x1, min_x2)
 init_z = get_gx(init_x1, init_x2)
 scatter_min = axes.scatter(min_x1, min_x2, min_z, color="red", linewidth=4, label="found minimum")
 scatter_init = axes.scatter(init_x1, init_x2, init_z, color="green", linewidth=4, label="init point")
 axes.legend(handles=[scatter_init, scatter_min], loc="upper left")