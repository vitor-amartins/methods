import matplotlib.pyplot
import math
from decimal import *

func = input("Type the function (y'): ");

def function(t, y):
    return eval(func);

height = 0
tf = 0
y = [];
t = [];
#PVI
y.append(Decimal(input("Type the y0: ")));
t.append(Decimal(input("Type the t0: ")));
#Menu options
print("1 - Enter height and number of steps(divisions)")
print("2 - Enter height and the tf")
print("3 - Enter number of steps(divisions) and the tf")
#Get chosen variables
opt = int(input())
if (opt == 1):
    height = Decimal(input("Type the h: "));
    n_steps = int(input("Type the n: "));
    tf = height * n_steps + t[0];
    print("tf = {}".format(tf));
elif (opt == 2):
    height = Decimal(input("Type the h: "));
    tf = Decimal(input("Type the tf: "));
    n_steps = (tf - t[0])/height;
    print("n = {}".format(n_steps));
elif(opt == 3):
    n_steps = int(input("Type the n: "));
    tf = Decimal(input("Type the tf: "));
    height = (tf-t[0])/n_steps;
#Order options
print("Choose the order of Adams-Bashforth")
print("1 - First order")
print("2 - Second order")
print("3 - Third order")
print("4 - Fourth order")
print("5 - Fifth order")
print("6 - Sixth order")
#Get the order
order = int(input())
#Adams-Bashforth
i = 0
if (order == 1):
    while t[i] < tf:
        i += 1
        y.append(Decimal(y[i-1] + (height)*(function(t[i-1], y[i-1]))))
        t.append(Decimal(t[i-1] + height))
        # If you want to see each iteration:
        # print("y({}) = {}".format(t[i], y[i]));
elif (order == 2):
    i += 1
    print("About the point (y1, f1): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    while t[i] < tf:
        i += 1
        y.append(Decimal(y[i-1] + (height/2)*(3*function(t[i-1], y[i-1]) - function(t[i-2], y[i-2]))))
        t.append(Decimal(t[i-1] + height))
        # If you want to see each iteration:
        # print("y({}) = {}".format(t[i], y[i]));
elif (order == 3):
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
        y.append(Decimal(y[i-1] + (height/12)*(23*function(t[i-1], y[i-1]) - 16*function(t[i-2], y[i-2]) + 5*function(t[i-3], y[i-3]))))
        t.append(Decimal(t[i-1] + height))
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
    i += 1
    print("About the point (y3, f3): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    while t[i] < tf:
        i += 1
        y.append(Decimal(y[i-1] + (height/24)*(55*function(t[i-1], y[i-1]) - 59*function(t[i-2], y[i-2]) + 37*function(t[i-3], y[i-3]) - 9*function(t[i-4], y[i-4]))))
        t.append(Decimal(t[i-1] + height));
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
    i += 1
    print("About the point (y4, f4): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    while t[i] < tf:
        i += 1
        y.append(Decimal(y[i-1] + (height/720)*(1901*function(t[i-1], y[i-1]) - 2774*function(t[i-2], y[i-2]) + 2616*function(t[i-3], y[i-3]) - 1274*function(t[i-4], y[i-4]) + 251*function(t[i-5], y[i-5]))))
        t.append(Decimal(t[i-1] + height));
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
    i += 1
    print("About the point (y5, f5): ")
    t.append(Decimal(t[i - 1] + height))
    y.append(Decimal(input("Type the 'y' of the point: ")))
    while t[i] < tf:
        i += 1
        y.append(Decimal(y[i-1] + (height/1440)*(4227*function(t[i-1], y[i-1]) - 7923*function(t[i-2], y[i-2]) + 9982*function(t[i-3], y[i-3]) - 7298*function(t[i-4], y[i-4]) + 2877*function(t[i-5], y[i-5]) - 475*function(t[i-6], y[i-6]))))
        t.append(Decimal(t[i-1] + height));
        # If you want to see each iteration:
        # print("y({}) = {}".format(t[i], y[i]));
else:
    exit (1)

#Output
print("y({}) = {}".format(tf, y[len(y)- 1]))
matplotlib.pyplot.title("Adams-Bashforth")
matplotlib.pyplot.xlabel("t")
matplotlib.pyplot.ylabel("y")
matplotlib.pyplot.grid(True)
matplotlib.pyplot.plot(t,y)
matplotlib.pyplot.show()