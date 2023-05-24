import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sympy import *

def multiple_roots_method(x0, tol, f, niter):
    """
    Performs the multiple roots method for finding roots of a given function.

    Parameters:
    - x0 (float): Initial guess value.
    - tol (float): Tolerable error to determine the convergence of the method.
    - f (sympy expression): The function for which to find the root.
    - niter (int): Maximum number of iterations allowed.

    Returns:
    None
    """

    v = symbols('v')  # Define the variable

    fder1 = f.diff(v)  # First derivative
    fder2 = f.diff(v, v)  # Second derivative

    # Initialization
    error = 100
    n = 0

    # Lists to store the approximations and corresponding function values
    approximations = []

    while error >= tol:
        xr = x0 - ((f.evalf(subs={v: x0})) * (fder1.evalf(subs={v: x0}))) / (
                    (fder1.evalf(subs={v: x0})) ** 2 - ((f.evalf(subs={v: x0})) * (fder2.evalf(subs={v: x0}))))
        error = abs(xr - x0)
        x0 = xr
        n += 1
        approximations.append(xr)
        print('Iteration:', n, 'Root:', x0, 'Error:', error)

        if n == niter:
            print("Method Failed within", n, "iterations")
            break

    # Plot the function and the approximations
    sns.set_style('whitegrid')
    plt.figure(figsize=(10, 6))

    v_vals = np.linspace(float(min(approximations)) - 3.0, float(max(approximations)) + 3.0, 500)
    f_vals = np.array([f.evalf(subs={v: x_val}) for x_val in v_vals])

    plt.plot(v_vals, f_vals, label='Function')
    plt.scatter(approximations, [f.evalf(subs={v: x_val}) for x_val in approximations], color='red',
                label='Approximations')
    plt.axhline(y=0, color='black', linestyle='--', label='y=0')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Multiple Roots Method - Approximations and Function')

    plt.legend()
    plt.show()


# Define the variable and function
v = symbols('v')
f = sympify("0.5 * 1.225 + cos(v) * v ** 2 * 15.165 * (2 * pi * 0.0872665) / (1 + (2 / 7.32))")

# Set initial guess, tolerable error, and maximum number of iterations
x0 = -2
tol = 0.5e-5
niter = 100

# Call the multiple roots method
multiple_roots_method(x0, tol, f, niter)
