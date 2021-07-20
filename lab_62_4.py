import matplotlib.pyplot as plt
import numpy as np

def stairs():
    n = int(input("Введите значение n "))
    x = np.linspace(-10, n, 1000)
    y = np.zeros([len(x)])
    for j in range (0, n+1, 1):
        for i in range(0, len(x), 1):
            if x[i]>j and x[i]>j+1:
                y[i] = j
    plt.plot(x,y)
    plt.show()

stairs()