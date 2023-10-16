import matplotlib.pyplot as plt
import numpy as np
from typing import Union

def get_fx(x: Union[int, float]) -> Union[int, float]:
 """
 Get the value of function f(x) in point x
 """
 return np.sin(np.pi * x) + x**2


def plot_fx(start_x: Union[int, float], end_x: Union[int, float], number_point: int):
 x = np.linspace(start_x, end_x, number_point)
 y = get_fx(x)
 plt.plot(x, y, label="f(x)")
 plt.title(r'$f(x)=sin(πx) + x^2$')
 plt.xlabel("x")
 plt.ylabel("f (x)")
 plt.grid()

def plot_fx_with_minimum(start_x: Union[int, float], end_x: Union[int, float], number_point: int, init_x: Union[int, float], min_x: Union[int, float]):
  plot_fx(start_x, end_x, number_point)
  min_y = get_fx(min_x)
  init_y = get_fx(init_x)
  plt.plot(min_x, min_y, marker='o', ls='none', ms=10, label="found min")
  plt.plot(init_x, init_y, marker='*', ls='none', ms=10, label="starting point")
  plt.legend(loc="best")

