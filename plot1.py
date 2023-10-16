import matplotlib.pyplot as plt
import numpy as np
from gradient_descent import gradient_descent_fx
from save_plot_data_to_file import save_plot
def get_fx(x):
 return np.sin(np.pi * x) + x**2

# first plot
x = np.linspace(-6, 6, 2000)  

y = get_fx(x)


dataArray = [
 {
 "init_value": -6,
 "learn_rate": 0.02,
 },
 {
  "init_value": -6,
  "learn_rate": 0.1,
 },
 {
  "init_value": -6,
  "learn_rate": 0.01,
 },
  {
  "init_value": -6,
  "learn_rate": 0.01,
 },
  {
  "init_value": -6,
  "learn_rate": 0.01,
 },
  {
  "init_value": -4,
  "learn_rate": 0.01,
 },
  {
  "init_value": -4,
  "learn_rate": 0.01,
 },
  {
  "init_value": -4,
  "learn_rate": 0.01,
 },
  {
  "init_value": -4,
  "learn_rate": 0.01,
 },
  {
  "init_value": -4,
  "learn_rate": 0.01,
 },
  {
  "init_value": -2,
  "learn_rate": 0.01,
 },
 {
  "init_value": -2,
  "learn_rate": 0.01,
 },
 {
  "init_value": -2,
  "learn_rate": 0.01,
 },
 {
  "init_value": -2,
  "learn_rate": 0.01,
 },
 {
  "init_value": -2,
  "learn_rate": 0.01,
 },
 {
  "init_value": 0,
  "learn_rate": 0.01,
 },
 {
  "init_value": 0,
  "learn_rate": 0.01,
 },
 {
  "init_value": 0,
  "learn_rate": 0.01,
 },
 {
  "init_value": 0,
  "learn_rate": 0.01,
 },
 {
  "init_value": 0,
  "learn_rate": 0.01,
 },
 {
  "init_value": 0.77,
  "learn_rate": 0.01,
 },
 {
  "init_value": 0.77,
  "learn_rate": 0.01,
 },
 {
  "init_value": 0.77,
  "learn_rate": 0.01,
 },
 {
  "init_value": 0.77,
  "learn_rate": 0.01,
 },
 {
  "init_value": 0.77,
  "learn_rate": 0.01,
 },
 {
  "init_value": 2,
  "learn_rate": 0.01,
 },
 {
  "init_value": 2,
  "learn_rate": 0.01,
 },
 {
  "init_value": 2,
  "learn_rate": 0.01,
 },
 {
  "init_value": 2,
  "learn_rate": 0.01,
 },
 {
  "init_value": 2,
  "learn_rate": 0.01,
 },
]
for data_entry in dataArray:
 data_entry["found_min"] = gradient_descent_fx(data_entry["init_value"], data_entry["learn_rate"], 1000)

save_plot(1, dataArray)

for data_entry in dataArray:
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
