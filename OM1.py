import math
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


def f(x):
    return (x ** 2 - 4) ** 2 / 9 - 1


def plot(l, r):
    ax = plt.gca()
    ax.set_ylim(-3, 50)

    x = np.linspace(l, r, num=100)
    plt.plot(x, f(x), "k-")


def bisection(l, r, e):
    L = r - l
    xm = (l + r) / 2

    plot(l, r)

    while L >= e:
        x1 = l + L / 4
        x2 = r - L / 4
        fx1 = f(x1)
        fx2 = f(x2)
        fxm = f(xm)
        plt.plot(x1, fx1, "c|")
        plt.plot(x2, fx2, "c|")

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


    plt.plot(xm, f(xm), "rx")
    plt.show()
    return xm


def golden(l, r, e):
    L = r - l
    t = (-1 + math.sqrt(5)) / 2
    x1 = r - t * L
    x2 = l + t * L

    plot(l, r)

    while L >= e:

        fx1 = f(x1)
        fx2 = f(x2)

        plt.plot(x1, fx1, "c|")
        plt.plot(x2, fx2, "c|")
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

    plt.show()
    return x1


def newton(x0, e):
    x = sym.Symbol('x')

    df1 = sym.lambdify(x, sym.diff((x ** 2 - 4) ** 2 / 9 - 1, x))
    df2 = sym.lambdify(x, sym.diff((x ** 2 - 4) ** 2 / 9 - 1, x, 2))

    curr = x0 - df1(x0) / df2(x0)
    prev = x0

    plot(0, 10)

    while abs(prev - curr) >= e:
        plt.plot(prev, f(prev), "c|", markersize=15)
        plt.plot(curr, f(curr), "c|", markersize=15)
        prev = curr
        curr = prev - df1(prev) / df2(prev)

    plt.plot(curr, f(curr), "rx")
    plt.show()

    return curr


def main():
    e = 0.00001
    l = 0
    r = 10
    minimum = bisection(l, r, e)
    print ("bisection results:\n",
           "minimum value: ", minimum)

    minimum = golden(l, r, e)
    print ("golden ratio results:\n",
           "minimum value: ", minimum)

    minimum = newton(5, e)
    print("golden ratio results:\n",
          "minimum value: ", minimum)


if __name__ == "__main__":
    main()
