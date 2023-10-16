from typing import Union
import numpy as np
from get_gradient import get_gradient_fx, get_gradient_gx

def gradient_descent_fx(init_value: Union[int, float], learn_rate: Union[int, float], max_iteration_count=500) -> float:
 """
 Get a point, which represents found minimum of function f(x) using gradient descent algorithm
 """
 curr_value = init_value
 for i in range(max_iteration_count):
  curr_value = curr_value - learn_rate*get_gradient_fx(curr_value)
 return round(curr_value, 2)

def gradient_descent_gx(init_point: np.ndarray, learn_rate: Union[int, float], max_iteration_count=500) -> np.ndarray:
 """
 Get a point, which represents found minimum of function g(x) using gradient descent algorithm
 """
 if init_point.shape != (2,):
  raise TypeError("Only ndarray with size 2x1 can represent a point for function g(x)!")
 
 curr_value = init_point
 for i in range(max_iteration_count):
  curr_value = curr_value - learn_rate*get_gradient_gx(curr_value)

 return np.array([round(curr_value[0], 2), round(curr_value[1], 2)])