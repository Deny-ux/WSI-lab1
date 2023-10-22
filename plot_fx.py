##############################################
#
# Author: Denys Fokashchuk, 323944 
#
##############################################

import matplotlib.pyplot as plt
import numpy as np
from typing import Union

title = r'$f(x)=sin(πx) + x^2$'

def get_fx(x: Union[int, float]) -> Union[int, float]:
	"""
	Get the value of function f(x) in point x
	"""
	return np.sin(np.pi * x) + x**2


def plot_fx(start_plot_x: Union[int, float], end_plot_x: Union[int, float], number_point: int):
	"""
	Makes a plot of function f(x)
	"""
	x = np.linspace(start_plot_x, end_plot_x, number_point)
	y = get_fx(x)
	plt.plot(x, y, label="f(x)")
	plt.title(title)
	plt.xlabel("x")
	plt.ylabel("f (x)")
	plt.grid()

def plot_fx_with_minimum(start_plot_x: Union[int, float], end_plot_x: Union[int, float], number_point: int, start_x: Union[int, float], learn_rate: Union[int, float], min_x: Union[int, float]):
	"""
	Makes a plot of function f(x), starting point, minimum point
	"""
	plot_fx(start_plot_x, end_plot_x, number_point)
	plt.title(title + f", learning rate={learn_rate}")
	min_y = get_fx(min_x)
	start_y = get_fx(start_x)
	plt.plot(min_x, min_y, marker='o', ls='none', ms=7, label="found min")
	plt.plot(start_x, start_y, marker='*', ls='none', ms=10, label="starting point")
	plt.legend(loc="best")

def plot_fx_with_every_minimum(start_plot_x: Union[int, float], end_plot_x: Union[int, float], number_point: int, values: list[float], learn_rate: Union[int, float]):
	"""
	Makes a plot of function f(x), every point, which was found using gradient descent
	"""
	plot_fx(start_plot_x, end_plot_x, number_point)
	fx_values =  list(map(get_fx, values))
	plt.title(title + f", learning rate={learn_rate}")
	plt.plot(values, fx_values, 'o--', color="orange", linestyle="--", ms=4,label="gradient descent")
	plt.plot(values[-1], get_fx(values[-1]), marker='o', color="red", ls='none', ms=7, label="found min")
	plt.plot(values[0], get_fx(values[0]), marker='*', color="green", ls='none', ms=10, label="starting point")  
	plt.legend(loc="best")