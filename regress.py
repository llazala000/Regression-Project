import numpy as np
from numpy import random
import matplotlib.pyplot as plt



hash_of_Lisbeth = "9D2BC5D19015F5CAE2055E7D4BE70982"
b0 = 1.2278983379844102
b1 = 1.125670170004326
random.seed(3792002685) #RNG
std = 0.59298819424258 #standard deviation
n = 100 #population size

xs = []
for i in range(n):
    xs.append(random.random())
print("predictors: ",xs)

ys = []
for i in range(n):
    ys.append((b0+(b1*xs[i])+ random.normal(0,std)))
print("population response:",ys)

for i in range (n):
    g = b0 + b1*xs[i]

x_ten_sample = []
y_ten_sample = []
for j in range(1,n):
    if (j%10 == 0):
        x_ten_sample.append(xs[j])
        y_ten_sample.append(ys[j])
x_ten_sample.append(xs[99])
y_ten_sample.append(ys[99])
print("10% sample of x:",x_ten_sample)
print("10% sample of y:", y_ten_sample)

colors = (0,0,0)
for i in range(n):
    plt.scatter(xs[i],ys[i],c=colors)
    plt.plot(b0+b1*xs[i],c='red')
    plt.title('Population & its regression model')
    plt.xlabel('x')
    plt.ylabel('y')
fit = np.polyfit(xs,ys,1)
fit_fn = np.poly1d(fit)
plt.plot(xs,ys,'yo', xs, fit_fn(xs), '--k')
plt.show()

for i in range(9):
    plt.scatter(x_ten_sample[i],y_ten_sample[i],c=colors)
    plt.title('Sample of the population & the population regression model')
    plt.xlabel('x')
    plt.ylabel('y')
fit1 = np.polyfit(x_ten_sample,y_ten_sample,1)
fit_fn1 = np.poly1d(fit)
plt.plot(x_ten_sample,y_ten_sample,'yo', x_ten_sample, fit_fn(x_ten_sample), '--k')
plt.show()


