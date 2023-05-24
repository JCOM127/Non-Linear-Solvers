import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sympy import *
import sys

def newton_root_finding(x0, tol, f, niter):
    """
    Performs Newton's root finding method for a given function.

    Parameters:
    - x0 (float): Initial guess value.
    - tol (float): Tolerable error to determine the convergence of the method.
    - f (sympy expression): The function for which to find the root.
    - niter (int): Maximum number of iterations allowed.

    Returns:
    Graph of the function and pretty prints table with Number of iterations, Approximation, Function evaluated and error.
    """

    v = symbols('v')  # Define the variable

    f_derivative = f.diff(v)  # Find the first derivative

    # Initialize variables
    xi = x0
    tramo = abs(2 * x0)
    n = 0

    # Lists to store the approximations and corresponding function values
    approximations = []
    function_values = []

    while tramo > tol and n < niter and f_derivative.evalf(subs={v: x0}) != 0:
        n += 1
        xn = xi - (f.evalf(subs={v: xi})) / (f_derivative.evalf(subs={v: xi}))  # Evaluate
        tramo = abs(xn - xi)  # Error, if Corr Dec
        xi = xn
        fn = f.evalf(subs={v: xn})
        approximations.append(xn)
        function_values.append(fn)
        print("N:", n, "Xn:", xn, "fn:", fn, "Error:", tramo)
        if n == niter:
            print("Root was not found within", n, "iterations")
        elif f_derivative.evalf(subs={v: xn}) == 0:
            print("Differential equals zero")
            break
        elif f_derivative.evalf(subs={v: xn}) > sys.float_info.max or f_derivative.evalf(subs={v: xn}) < sys.float_info.min:
            print(f_derivative.evalf(subs={v: xn}), "Overflows, then will not converge within", n, "iterations")
            break

    # Output (n, xn, fn, Error).

    # Plot the function and the approximations
    sns.set_style('whitegrid')
    plt.figure(figsize=(10, 6))

    v_vals = np.linspace(float(min(approximations)) - 3.0, float(max(approximations)) + 3.0, 500)
    f_vals = np.array([f.evalf(subs={v: x_val}) for x_val in v_vals])

    plt.plot(v_vals, f_vals, label='Function')
    plt.scatter(approximations, function_values, color='red', label='Approximations')
    plt.axhline(y=0, color='black', linestyle='--', label='y=0')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Newton Method - Approximations and Function')

    plt.legend()
    plt.show()

# Define the variable and function
v = symbols('v')
f = sympify("0.5 * 1.225 + cos(v) * v ** 2 * 15.165 * (2 * pi * 0.0872665) / (1 + (2 / 7.32))")

# Set initial guess, tolerable error, and maximum number of iterations
x0 = -2
tol = 0.5e-5
niter = 100

# Call the Newton's root finding method
newton_root_finding(x0, tol, f, niter)
