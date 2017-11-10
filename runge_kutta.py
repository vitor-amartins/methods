import matplotlib.pyplot
import math
from decimal import *

func = input("Type the function (y'): ");

def function(t, y):
    return eval(func);

y = [];
t = [];
#PVI
y.append(Decimal(input("Type the y0: ")))
t.append(Decimal(input("Type the t0: ")))
#Menu options
print("1 - Enter height and number of steps(divisions)")
print("2 - Enter height and the tf")
print("3 - Enter number of steps(divisions) and the tf")
opt = int(input())
#Get chosen variables
if (opt == 1):
    height = Decimal(input("Type the h: "))
    n_steps = int(input("Type the n: "))
    tf = height * n_steps + t[0]
    print("tf = {}".format(tf))
elif (opt == 2):
    height = Decimal(input("Type the h: "))
    tf = Decimal(input("Type the tf: "))
    n_steps = (tf - t[0])/height
    print("n = {}".format(n_steps))
elif(opt == 3):
    n_steps = int(input("Type the n: "))
    tf = Decimal(input("Type the tf: "))
    height = (tf-t[0])/n_steps;
#Runge-Kutta
i = 0;
while t[i] < tf:
    i += 1;
    yn = y[i - 1]
    tn = t[i - 1]
    k1 = Decimal(function(tn, yn))
    k2 = Decimal(function(tn + Decimal(0.5)*height, yn + Decimal(0.5)*height*k1))
    k3 = Decimal(function(tn + Decimal(0.5)*height, yn + Decimal(0.5)*height*k2))
    k4 = Decimal(function(tn + height, yn + height*k3))

    y.append(Decimal(yn + ((height * (k1 + 2*k2 + 2*k3 + k4) )/6) ))
    t.append(Decimal(tn + height))
    #If you want to see each iteration:
    #print("y({}) = {}".format(t[i], y[i]));
#Output
print("y({}) = {}".format(tf, y[len(y)- 1]))
matplotlib.pyplot.title("Runge-Kutta")
matplotlib.pyplot.xlabel("t")
matplotlib.pyplot.ylabel("y")
matplotlib.pyplot.grid(True)
matplotlib.pyplot.plot(t,y);
matplotlib.pyplot.show()