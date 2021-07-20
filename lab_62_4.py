import matplotlib.pyplot as plt
import numpy as np

def stairs():
    n = int(input("Введите значение n "))
    x = np.linspace(-10, 10, 100)
    y = np.zeros([len(x)])
    N = np.linspace(0, n, n+1)
    k = len(x)/n
    round(k)
    a = 0
    i = 0
    while a != len(x):
        while i*k>a:
            y[a] = N[i]
            a = a + 1
        k = k+1
    plt.plot(x,y)
    plt.show()

stairs()