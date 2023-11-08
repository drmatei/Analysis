import numpy as np
import matplotlib.pyplot as plt


def convex_f(x: int):
    return x ** 2


def derivative_of_convex_f(x: int):
    return 2 * x


def not_convex_f(x: int):
    return x ** 3 - 3 * x


def derivative_of_not_convex(x: int):
    return 3 * x ** 2 - 3

def gradient_descent_method(eta):

