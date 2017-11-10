import matplotlib.pyplot
import math
from decimal import *

func = input("Type the function (y'): ")

def function(t, y):
    return eval(func)

tf = 0
y = []
t = []
y_prev = []
#PVI
y.append(Decimal(input("Type the y0: ")))
t.append(Decimal(input("Type the t0: ")))
y_prev.append(y[0])
#Menu options
print("Choose one:")
print("1 - Enter height and number of steps(divisions)")
print("2 - Enter height and the tf")
print("3 - Enter number of steps(divisions) and the tf")
opt = int(input())
#Get chosen variables
if (opt == 1):
    height = Decimal(input("Type the h: "))
    n_steps = int(input("Type the n: "))
    tf = height * n_steps + t[0]
elif (opt == 2):
    height = Decimal(input("Type the h: "))
    tf = Decimal(input("Type the tf: "))
    n_steps = (tf - t[0])/height
elif(opt == 3):
    n_steps = int(input("Type the n: "))
    tf = Decimal(input("Type the tf: "))
    height = (tf-t[0])/n_steps
else:
    exit (1)
#Euler modified
i = 0
while t[i] < tf:
    i += 1
    yn = y[i-1]
    tn = t[i-1]
    y_preview = Decimal(yn + function(tn, yn)*height)
    y_prev.append(y_preview)
    t.append(Decimal(tn + height))
    y.append(Decimal(yn + height*(Decimal(function(tn, yn) + function(t[i], y_preview))/2)))
#Output
print("y({}) = {}".format(tf, y[len(y)- 1]))
matplotlib.pyplot.title("Euler modified")
matplotlib.pyplot.xlabel("t")
matplotlib.pyplot.ylabel("y")
matplotlib.pyplot.grid(True)
matplotlib.pyplot.plot(t,y)
matplotlib.pyplot.show()