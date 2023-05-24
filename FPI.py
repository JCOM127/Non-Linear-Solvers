import math
import numpy as np
import matplotlib.pyplot as plt

def f(v):
    return 0.5 * 1.225 + math.cos(v) * v ** 2 * 15.165 * (2 * (math.pi) * 0.0872665) / (1 + (2 / 7.32))  # initial function

def g(v):
    return np.arccos((0.5 * 1.225 - f(v)) * (1 + (2 / 7.32)) / (v ** 2 * 15.165 * (2 * (np.pi) * 0.0872665)))  # conditioning function

def fixedPointIteration(x0, e, niter):
    n = 0
    err = 1
    fx = f(x0)
    xn = x0

    if fx == 0:
        print(x0, "is already a root")

    iterations = []
    approximations = []

    while err > e and n < niter:
        n += 1
        xn = g(x0)
        x0 = xn
        fm = f(xn)  # Assign fm here
        err = abs(xn - x0)  # error, if Corr Dec
        # err = abs((xn - x0) / xn)  # error, if Sig Fig
        print("N:", n, "xn:", xn, "fm:", fm, "Error:", err)
        iterations.append(n)
        approximations.append(xn)

    if fm == 0:
        print(x0, "is a root")
    elif err <= e:
        print(x0, "is a root of the function in", n, "iterations")

    # Plotting the function and approximations
    v = np.linspace(0, 2 * np.pi, 100)
    plt.plot(v, [f(x) for x in v], label='Function f(v)')
    plt.scatter(approximations, [f(x) for x in approximations], color='red', label='Approximations')
    plt.xlabel('v')
    plt.ylabel('f(v)')
    plt.title('Fixed-Point Iteration')
    plt.legend()
    plt.grid(True)
    plt.show()

# Input Section
x0 = float(input('Enter initial guess: '))
e = float(input('Tolerable Error: '))
niter = int(input('Maximum Iterations: '))

fixedPointIteration(x0, e, niter)
