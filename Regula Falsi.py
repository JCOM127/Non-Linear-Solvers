import math
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def f(v):
    """
    Function to evaluate the given function at a specific value.

    Parameters:
    - v (float): The value at which to evaluate the function.

    Returns:
    - float: The result of evaluating the function at the given value.
    """
    return 0.5 * 1.225 + math.cos(v) * v ** 2 * 15.165 * (2 * (math.pi) * 0.0872665) / (1 + (2 / 7.32))


def falsePosition(x0, x1, e):
    """
    Regula Falsi method for finding the root of a function within a given interval.

    Parameters:
    - x0 (float): The first guess value.
    - x1 (float): The second guess value.
    - e (float): Tolerable error to determine the convergence of the method.

    Returns:
    None
    """
    step = 1
    condition = True

    # Store the approximations and corresponding function values
    approximations = []
    function_values = []

    while condition:
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        error = abs(x2 - x1)
        print('Iteration-%d, x2 = %0.6f, f(x2) = %0.6f, Error = %0.6f' % (step, x2, f(x2), error))

        approximations.append(x2)
        function_values.append(f(x2))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step += 1
        condition = abs(f(x2)) > e

    print('\nRequired root is: %0.8f' % x2)

    # Determine the x-axis limits for plotting
    x_min = min(approximations + [x0, x1])
    x_max = max(approximations + [x0, x1])

    # Plot the function and the approximations
    sns.set_style('whitegrid')
    plt.figure(figsize=(10, 6))

    v = np.linspace(x_min, x_max, 100)
    plt.plot(v, [f(x) for x in v], label='Function')
    plt.scatter(approximations, function_values, color='red', label='Approximations')
    plt.axhline(y=0, color='black', linestyle='--', label='y=0')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Regula Falsi Method - Approximations and Function')

    plt.legend()
    plt.show()


# Input Section
x0 = float(input('First Guess: '))
x1 = float(input('Second Guess: '))
e = float(input('Tolerable Error: '))

# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0, x1, e)
