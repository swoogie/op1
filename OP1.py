import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (x ** 2 - 4) ** 2 / 9 - 1


def bisection(l, r, e):
    L = r - l
    xm = (l + r) / 2

    plt.figure(num=0, dpi=120)
    ax = plt.gca()
    ax.set_ylim(-3, 50)

    x = np.linspace(l, r, num=100)
    plt.plot(x, f(x), "k-")

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

def main():
    e = 0.00001
    l = 0
    r = 10
    minimum = bisection(l, r, e)
    print ("minimum value: ", minimum)

if __name__ == "__main__":
    main()

    