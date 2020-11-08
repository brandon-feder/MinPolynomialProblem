import numpy as np
import sys
from sympy import *

def sum(arr, A, B):
    sum = 0;
    for x in arr:
        sum += x[0]**A*x[1]**B
    return sum

#parameters are bounds, f(x) nP points, and the degree
def solve(b, F, nP, k):
    x = [ F((b[1]-b[0])*x/(nP-1) + b[0]) for x in range(0, nP) ] # May be issue if b[0] > b[1]
    y = [ (b[1]-b[0])*x/(nP-1) + b[0] for x in range(0, nP) ]

    # x = [ -3, -2, -1, -0.2, 1, 3 ]
    # y = [0.9, 0.8, 0.4, 0.2, 0.1, 0]

    M = [ [
        sum( ( (xi, 1) for xi in x ), j+i, 1 )
    for j in range(k+1) ] for i in range(k+1) ]

    b = [ sum( [ (x[i], y[i]) for i in range(len(x))], i, 1) for i in range(k+1) ]

    M = np.array( M, dtype=np.double ).reshape(k+1, k+1)
    b = np.array( b, dtype=np.double ).reshape(k+1, 1 )

    # print(M)
    # print(b)

    a = np.linalg.inv(M).dot(b)

    s = ""
    for i in range(len(a)):
        if i > 0:
            s += " + "
        s += str(a[len(a)-i-1][0])
        if(len(a)-i-1 > 1):
            s += "x^" + str(len(a)-i-1)
        elif(len(a)-i-1 > 0):
            s += "x"
    print(s)
def __main__():
    # f(x) = _______________ written in python eg: x**2 represents x to the second power
    f_raw = sys.argv[1]

    # bounds of the function to solve for
    bounds = (int(sys.argv[2]), int(sys.argv[3]))

    # Points being used is accuracy*depth*|b-a|
    accuracy = int(sys.argv[4])

    print("f(x) = {}".format(f_raw))
    print("bounds are [{}, {}]".format(bounds[0], bounds[1]))

    f = lambda x: eval(f_raw)
    solve(bounds, f, accuracy, int(sys.argv[5]))

__main__()
