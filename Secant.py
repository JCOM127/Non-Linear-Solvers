import math
import seaborn as sns
import matplotlib.pyplot as plt

def f(v):
    """
    Function to evaluate the given function at a specific value.

    Parameters:
    - v (float): The value at which to evaluate the function.

    Returns:
    - float: The result of evaluating the function at the given value.
    """
    return 0.5 * 1.225 + math.cos(v) * v ** 2 * 15.165 * (2 * (math.pi) * 0.0872665) / (1 + (2 / 7.32))


def secant(f, x1, x2, tol, niter):
    """
    Secant method for finding the root of a function.

    Parameters:
    - f (function): The function for which to find the root.
    - x1 (float): The first initial guess value.
    - x2 (float): The second initial guess value.
    - tol (float): Tolerable error to determine the convergence of the method.
    - niter (int): Maximum number of iterations allowed.

    Returns:
    Graph of the function and pretty prints table with Number of iterations, Approximation, Function evaluated and error.
    """
    n = 0
    x3 = 0
    err = 10

    if f(x1) == f(x2):
        raise ZeroDivisionError("Cannot proceed")

    # Store the approximations and corresponding function values
    approximations = []
    function_values = []

    while err > tol and n < niter:
        n += 1
        x3 = x1 - (x2 - x1) * f(x1) / (f(x2) - f(x1))
        err = abs(x3 - x2)
        x1 = x2
        x2 = x3
        approximations.append(x3)
        function_values.append(f(x3))
        print("N:", n, "xn:", x3, "fm", f(x3), "Error:", err)

    if err <= tol:
        print("\nOn iteration:", n, ", a root was obtained at:", x3, ", function returns:", f(x3))
    elif n == niter:
        print("Method failed within", n, "iterations")

    # Plot the function and the approximations
    sns.set_style('whitegrid')
    plt.figure(figsize=(10, 6))
    v = [x for x in range(int(min(approximations)) - 2, int(max(approximations)) + 2)]
    plt.plot(v, [f(x) for x in v], label='Function')
    plt.scatter(approximations, function_values, color='red', label='Approximations')
    plt.axhline(y=0, color='black', linestyle='--', label='y=0')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Secant Method - Approximations and Function')
    plt.legend()
    plt.show()


# Input Section
x1 = float(input('Enter interval A: '))
x2 = float(input('Enter interval B: '))
e = float(input('Tolerable Error: '))
niter = int(input('Maximum Step: '))

# Apply the secant method
secant(f, x1, x2, e, niter)
