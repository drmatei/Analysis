import numpy as np
import matplotlib.pyplot as plt


def convex_f(x: int):
    return x ** 2


def derivative_of_convex_f(x: int):
    return 2 * x


def nonconvex_f(x: int):
    return x ** 3 - 2 * x


def derivative_of_nonconvex_f(x: int):
    return 3 * x ** 2 - 2


def gradient_descent_method(initial_x, learning_rate, iterations, convex):
    x = initial_x
    values = []
    if convex:
        for _ in range(iterations):
            values.append(x)
            x = x - learning_rate * derivative_of_convex_f(x)
    else:
        for _ in range(iterations):
            values.append(x)
            x = x - learning_rate * derivative_of_nonconvex_f(x)
    return values


def plot_function_and_path(x, func, path, title):
    plt.plot(x, func(x), label='Function')
    plt.scatter(path, [func(xi) for xi in path], color='red', label='Gradient_Descent_Path')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title(title)
    plt.show()


while True:
    user_choice = int(input("""Gradient Descent - tests:
1. Convergence with a small learning rate (f-convex)
2. Convergence with a bigger learning rate (f-convex)
3. Divergence because learning rate is too large (f-convex)
4. Descent getting stuck in a local minimum because we take a nonconvex f 
5. Exit 
>"""))

    if user_choice == 1:
        learning_rate_small_teeny_tiny = 0.1
        x0 = 3
        iterations = 20
        path = gradient_descent_method(x0, learning_rate_small_teeny_tiny, iterations, True)
        plot_function_and_path(np.linspace(-5, 5, 100), convex_f, path, "Converges with very small learning rate")

    elif user_choice == 2:
        learning_rate_bigger = 0.9
        x0 = 3
        iterations = 20
        path = gradient_descent_method(x0, learning_rate_bigger, iterations, True)
        plot_function_and_path(np.linspace(-5, 5, 100), convex_f, path, "Converges faster with a bigger learning rate")

    elif user_choice == 3:
        learning_rate_too_big = 1.2
        x0 = 2
        iterations = 5
        path = gradient_descent_method(x0, learning_rate_too_big, iterations, True)
        plot_function_and_path(np.linspace(-5, 5, 100), convex_f, path, "Diverges with learning rate too big")

    elif user_choice == 4:
        learning_rate = 0.01
        x0 = 0.9
        iterations = 100
        path = gradient_descent_method(x0, learning_rate, iterations, False)
        plot_function_and_path(np.linspace(-5, 5, 100), convex_f, path, "Stuck in a local function for a nonconvex f")

    elif user_choice == 5:
        print("Bye!!")
        break

    else:
        print("error")












