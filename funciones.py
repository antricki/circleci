import math


def suma(x, y):
    return x + y


def resta(x, y):
    return x - y


def multiplicacion(x, y):
    return x * y


def division(x, y):
    return x / y


def raiz(x):
    math.sqrt(x)


def factorial(n):
    if(n >= 0):
        factorial_total = 1
        while n > 1:
            factorial_total *= n
            n -= 1
        return factorial_total
    else:
        return math.nan
