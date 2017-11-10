import matplotlib.pyplot
import math
from decimal import *

func = input("Type the function (y'): ")

def function(t, y):
    return eval(func)

height = 0
tf = 0
y = [];
t = [];
#PVI
y.append(Decimal(input("Type the y0: ")))
t.append(Decimal(input("Type the t0: ")))
#Menu options
print("1 - Enter height and number of steps(divisions)")
print("2 - Enter height and the tf")
print("3 - Enter number of steps(divisions) and the tf")
#Get chosen variables
opt = int(input())
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
#Order options
print("Choose the order of Adams-Moulton")
print("1 - First order")
print("2 - Second order")
print("3 - Third order")
print("4 - Fourth order")
print("5 - Fifth order")
print("6 - Sixth order")
#Get the order
order = int(input())
#Adams-Moulton
i = 0
if (order == 1):
    while t[i] < tf:
        i += 1
        y_euler = y[i-1] + height*function(t[i-1], y[i-1])
        t.append(Decimal(t[i-1] + height))
        y.append(Decimal(y[i-1] + (height)*(function(t[i], y_euler))))
        # If you want to see each iteration:
        # print("y({}) = {}".format(t[i], y[i]));
elif (order == 2):
    while t[i] < tf:
        i += 1
        y_euler = y[i-1] + height*function(t[i-1], y[i-1])
        t.append(Decimal(t[i-1] + height))
        y.append(Decimal(y[i-1] + (height/2)*(function(t[i], y_euler) + function(t[i-1], y[i-1]))))
        # If you want to see each iteration:
        # print("y({}) = {}".format(t[i], y[i]));
elif (order == 3):
    i += 1
    print("About the point (y1, f1): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    while t[i] < tf:
        i += 1
        y_euler = y[i-1] + height*function(t[i-1], y[i-1])
        t.append(Decimal(t[i-1] + height))
        y.append(Decimal(y[i-1] + (height/12)*(5*function(t[i], y_euler) + 8*function(t[i-1], y[i-1]) - function(t[i-2], y[i-2]))))
        # If you want to see each iteration:
        # print("y({}) = {}".format(t[i], y[i]));
elif (order == 4):
    i += 1
    print("About the point (y1, f1): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    i += 1
    print("About the point (y2, f2): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    while t[i] < tf:
        i += 1
        y_euler = y[i-1] + height*function(t[i-1], y[i-1])
        t.append(Decimal(t[i-1] + height))
        y.append(Decimal(y[i-1] + (height/24)*(9*function(t[i], y_euler) + 19*function(t[i-1], y[i-1]) - 5*function(t[i-2], y[i-2]) + function(t[i-3], y[i-3]))))
        # If you want to see each iteration:
        # print("y({}) = {}".format(t[i], y[i]));
elif (order == 5):
    i += 1
    print("About the point (y1, f1): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    i += 1
    print("About the point (y2, f2): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    i += 1
    print("About the point (y3, f3): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    while t[i] < tf:
        i += 1
        y_euler = y[i-1] + height*function(t[i-1], y[i-1])
        t.append(Decimal(t[i-1] + height))
        y.append(Decimal(y[i-1] + (height/720)*(251*function(t[i], y_euler) + 646*function(t[i-1], y[i-1]) - 264*function(t[i-2], y[i-2]) + 106*function(t[i-3], y[i-3]) - 19*function(t[i-4], y[i-4]))))
        # If you want to see each iteration:
        # print("y({}) = {}".format(t[i], y[i]));
elif (order == 6):
    i += 1
    print("About the point (y1, f1): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    i += 1
    print("About the point (y2, f2): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    i += 1
    print("About the point (y3, f3): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    i += 1
    print("About the point (y4, f4): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    while t[i] < tf:
        i += 1
        y_euler = y[i-1] + height*function(t[i-1], y[i-1])
        t.append(Decimal(t[i-1] + height))
        y.append(Decimal(y[i-1] + (height/1440)*(475*function(t[i], y_euler) + 1427*function(t[i-1], y[i-1]) - 798*function(t[i-2], y[i-2]) + 482*function(t[i-3], y[i-3]) - 173*function(t[i-4], y[i-4]) + 27*function(t[i-5], y[i-5]))))
        # If you want to see each iteration:
        # print("y({}) = {}".format(t[i], y[i]));
else:
    exit (1)

#Output
print("y({}) = {}".format(tf, y[len(y)- 1]))
matplotlib.pyplot.title("Adams-Moulton")
matplotlib.pyplot.xlabel("t")
matplotlib.pyplot.ylabel("y")
matplotlib.pyplot.grid(True)
matplotlib.pyplot.plot(t,y)
matplotlib.pyplot.show()