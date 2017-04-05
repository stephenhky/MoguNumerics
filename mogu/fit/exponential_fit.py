from operator import add
from math import sqrt

golden_ratio = (sqrt(5) - 1) * 0.5


def sumSquaresErrors(xlist, ylist, alpha):
    if len(xlist) != len(ylist):
        return None
    return reduce(add, map(lambda x, y: (x ** alpha - y) ** 2, xlist, ylist))


def goldenSearchMin(func, x1, x2, tol=1e-5):
    if abs(x1 - x2) < tol:
        return x1
    xl = x1 + (x2 - x1) * (1 - golden_ratio)
    xr = x1 + (x2 - x1) * golden_ratio
    fl = func(xl)
    fr = func(xr)
    return goldenSearchMin(func, x1, xr, tol=tol) if fl <= fr else goldenSearchMin(func, xl, x2, tol=tol)

