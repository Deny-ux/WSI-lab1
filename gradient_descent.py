##############################################
#
# Author: Denys Fokashchuk, 323944 
#
##############################################


from typing import Union
import numpy as np
from get_gradient import get_gradient_fx, get_gradient_gx

def gradient_descent_fx(init_value: Union[int, float], learn_rate: Union[int, float], max_iteration_count=500) -> list[float]:
 """
 Returns an arrays of points, each element represents point in each iteration while 
 finding minimum of function f(x) using gradient descent algorithm
 Last element - found minimum
 """
 curr_value = init_value
 values = []
 for i in range(max_iteration_count):
  values.append(curr_value)
  curr_value = curr_value - learn_rate*get_gradient_fx(curr_value)
 return values

def gradient_descent_gx(init_point: np.ndarray, learn_rate: Union[int, float], max_iteration_count=500) -> list[np.ndarray]:
 """
 Returns an arrays of points, each element represents point in each iteration while 
 finding minimum of function g(x) using gradient descent algorithm
 Last element - found minimum
 """

 if init_point.shape != (2,):
  raise TypeError("Only ndarray with size 2x1 can represent a point for function g(x)!")
 
 values: list[np.ndarray] = []
 curr_value = init_point
 for i in range(max_iteration_count):
  values.append(np.array([curr_value[0], curr_value[1]]))
  curr_value = curr_value - learn_rate*get_gradient_gx(curr_value)
 return values