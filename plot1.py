import matplotlib.pyplot as plt
import numpy as np
from gradient_descent import gradient_descent_fx

def get_fx(x):
 return np.sin(np.pi * x) + x**2

# first plot
x = np.linspace(-3, 3, 2000)  

y = get_fx(x)

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
