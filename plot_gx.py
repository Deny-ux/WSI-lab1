##############################################
#
# Author: Denys Fokashchuk, 323944 
#
##############################################


import matplotlib.pyplot as plt
from gradient_descent import gradient_descent_gx
import numpy as np
from test_data import data_array_gx
from save_plot_data_to_file import save_function_data
from typing import Union, List

title = r'g(x)=5$e^{2}$ - 4e$x_1$ + $x_{1}^{2}$ + 2e$x_2$ + $x_{2}^{2}$'

def get_gx(x1: Union[int, float], x2: Union[int, float]):
	"""
	Get the value of function g(x) in point x1, x2
	"""
	return 5 * (np.e **2) - 4*np.e*x1 + x1**2 + 2*np.e*x2 + x2**2

def plot_surface_gx(axes, start_x: Union[int, float], end_x: Union[int, float], number_point_x: int, start_y: Union[int, float], end_y: Union[int, float], number_point_y: int):
	"""
	Makes a surface plot of function g(x)
	"""
	x = np.linspace(start_x, end_x, number_point_x)
	y = np.linspace(start_y, end_y, number_point_y)
	X, Y = np.meshgrid(x, y)
	Z = get_gx(X, Y)
	surface = axes.plot_surface(X, Y, Z, cmap="plasma")
	axes.set_xlabel('X1-axis')
	axes.set_ylabel('X2-axis')
	axes.set_zlabel('g(x)')
	axes.set_title(title)
	plt.colorbar(surface)

def plot_surface_gx_with_minimum(axes, start_x: Union[int, float], end_x: Union[int, float], number_point_x: int, start_y: Union[int, float], end_y: Union[int, float], number_point_y: int, init_x1:Union[int, float], init_x2: Union[int, float], min_x1: Union[int, float], min_x2: Union[int, float], learn_rate: Union[int, float]):
	"""
	Makes a surface plot of function g(x) with starting point, minimum point
	"""
	plot_surface_gx(axes, start_x, end_x, number_point_x, start_y, end_y, number_point_y)
	min_z = get_gx(min_x1, min_x2)
	init_z = get_gx(init_x1, init_x2)
	scatter_min = axes.scatter(min_x1, min_x2, min_z, color="red", linewidth=4, label="found min")
	scatter_init = axes.scatter(init_x1, init_x2, init_z, color="green", linewidth=4, label="starting point")
	axes.set_title(title + f", learning rate={learn_rate}")
	axes.legend(handles=[scatter_init, scatter_min], loc="upper left")

def plot_contour_gx(X: np.ndarray, Y: np.ndarray, Z: np.ndarray, radius:Union[int, float]):
	"""
	Makes a contour plot of function g(x)
	"""
	plt.contour(X, Y, Z, radius)
	plt.xlabel("x1")
	plt.ylabel("x2")
	plt.title(title)

def plot_contour_gx_with_minimum(X: np.ndarray, Y: np.ndarray, Z: np.ndarray, radius: Union[int, float], init_x1: Union[int, float], init_x2: Union[int, float], min_x1: Union[int, float], min_x2: Union[int, float],  learn_rate: Union[int, float]):
	"""
	Makes a contour plot of function g(x) with starting point, minimum point
	"""
	plot_contour_gx(X, Y, Z, radius)
	plt.title(title + f", learning rate={learn_rate}")
	plt.scatter(min_x1, min_x2, label="found min", c="orange")
	plt.scatter(init_x1, init_x2, label="starting point", c="green")
	plt.legend(loc="best")

def plot_contour_gx_with_every_minimum(X: np.ndarray, Y: np.ndarray, Z: np.ndarray, radius: Union[int, float], values: List[np.ndarray], learn_rate: Union[int, float]):
	"""
	Makes a contour plot of function g(x) with starting point, minimum point
	"""
	plot_contour_gx(X, Y, Z, radius)
	values_x1 = [value[0] for value in values]
	values_x2 = [value[1] for value in values]

	# plt.scatter(min_x1, min_x2, label="found min", c="orange")
	
	# plt.plot(values_x1, values_x2, 'ro', linestyle="solid", label="gradient descent")
	plt.plot(values_x1, values_x2, 'o--', color="orange", linestyle="--", ms=4,label="gradient descent")
	plt.plot(values_x1[-1], values_x2[-1], marker='o', color="red", ls='none', ms=7, label="found min")
	plt.plot(values_x1[0], values_x2[0], marker='*', color="green", ls='none', ms=10, label="starting point")
	plt.title(title + f", learning rate={learn_rate}")

	plt.legend()

