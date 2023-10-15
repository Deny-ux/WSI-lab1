import numpy as np
from typing import Union

def get_gradient_fx( point: Union[int, float]) -> float:
 
  if not (isinstance(point, int) or isinstance(point, float)):
   raise TypeError("Only int or float can represent a point for function f(x)!")
  return np.pi*np.cos(np.pi * point) + 2*point

 
def get_gradient_gx(point: np.ndarray) -> float:

 if point.shape != (2,):
  raise TypeError("Only ndarray with size 2x1 can represent a point for function g(x)!")

 x1 = point[0]
 x2 = point[1]
 return np.array([2*(x1 - 2 * np.e), 2* (x2 + np.e)])
 