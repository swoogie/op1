import math
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

count = 0


def f(x):
    global count
    count += 1
    return (x ** 2 - 4) ** 2 / 9 - 1  # function


def plot(l, r):
    ax = plt.gca()
    ax.set_ylim(-3, 50)

    x = np.linspace(l, r, num=100)
    plt.plot(x, f(x), "k-")


def plotPoint(x, f):
    plt.plot(x, f, "c|", markersize=15)


def bisection(l, r, e):
    global count

    L = r - l
    xm = (l + r) / 2

    plot(l, r)
    count = 0
    it = 0
    while L >= e:
        x1 = l + L / 4
        x2 = r - L / 4
        fx1 = f(x1)
        fx2 = f(x2)
        fxm = f(xm)
        plotPoint(x1, fx1)
        plotPoint(x2, fx2)

        if fx1 < fxm:
            r = xm
            xm = x1

        elif fx2 < fxm:
            l = xm
            xm = x2

        else:
            l = x1
            r = x2

        L = r - l
        it += 1

    plt.plot(xm, f(xm), "rx")
    plt.show()
    return xm, count, it


def golden(l, r, e):
    global count

    L = r - l
    t = (-1 + math.sqrt(5)) / 2
    x1 = r - t * L
    x2 = l + t * L

    plot(l, r)
    count = 0
    it = 0
    while L >= e:
        fx1 = f(x1)
        fx2 = f(x2)

        plotPoint(x1, fx1)
        plotPoint(x2, fx2)
        if fx2 < fx1:
            l = x1
            L = r - l
            x1 = x2
            x2 = l + t * L
        else:
            r = x2
            L = r - l
            x2 = x1
            x1 = r - t * L
        it += 1

    plt.plot(x1, f(x1), "rx")
    plt.show()
    return x1, count, it


def newton(x0, e):
    global count

    x = sym.Symbol('x')

    df1 = sym.lambdify(x, sym.diff(f(x), x))
    df2 = sym.lambdify(x, sym.diff(f(x), x, 2))

    curr = x0 - df1(x0) / df2(x0)
    prev = x0

    plot(0, 10)  # 0, 10 is x axis
    count = 0
    it = 0
    while abs(prev - curr) >= e:
        plotPoint(prev, f(prev))
        plotPoint(curr, f(curr))

        prev = curr
        curr = prev - df1(prev) / df2(prev)
        it += 1

    plt.plot(curr, f(curr), "rx")
    plt.show()

    return curr, count, it


def main():
    e = 0.00001  # accuracy
    l = 0  # left
    r = 10  # right
    minimum, count, it = bisection(l, r, e)
    print("bisection results:",
          "\nminimum value: ", minimum,
          "\nfunction was called: ", count, " times",
          "\nnumber of iterations: ", it)

    minimum, count, it = golden(l, r, e)
    print("golden ratio results:",
          "\nminimum value: ", minimum,
          "\nfunction was called: ", count, " times",
          "\nnumber of iterations: ", it)

    minimum, count, it = newton(5, e)  # 5 - starting point
    print("newton results:",
          "\nminimum value: ", minimum,
          "\nfunction was called: ", count, " times",
          "\nnumber of iterations: ", it)


if __name__ == "__main__":
    main()
