import matplotlib.pyplot
import math
from decimal import *

func = input("Type the function (y'): ")

def function(t, y):
    return eval(func)

tf = 0
y = []
t = []
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
    tf = height * n_steps + Decimal(t[0])
elif (opt == 2):
    height = Decimal(input("Type the h: "))
    tf = Decimal(input("Type the tf: "))
    n_steps = (tf - Decimal(t[0]))/height
elif(opt == 3):
    n_steps = int(input("Type the n: "))
    tf = Decimal(input("Type the tf: "))
    height = (tf- Decimal(t[0]))/n_steps
#Euler inverse
i = 0
while t[i] < tf:
    i += 1
    y_euler = y[i-1] + height*function(t[i-1], y[i-1])
    t.append(Decimal(t[i-1] + height))
    y.append(y[i-1] + height*function(t[i], y_euler))
    #If you want to see each iteration:
    #print("y({}) = {}".format(t[i], y[i]));
#Output
print("y({}) = {}".format(tf, y[len(y)- 1]))
matplotlib.pyplot.title("Euler inverse")
matplotlib.pyplot.xlabel("t")
matplotlib.pyplot.ylabel("y")
matplotlib.pyplot.grid(True)
matplotlib.pyplot.plot(t,y);
matplotlib.pyplot.show()