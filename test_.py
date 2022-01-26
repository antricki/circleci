import funciones
# import math


def test_suma():
    assert funciones.suma(4, 5) == 9


def test_resta():
    assert funciones.resta(5, 5) == 0


def test_multi():
    assert funciones.multiplicacion(2, 2) == 4


def test_div():
    assert funciones.division(2, 2) == 1


def test_factorial():
    assert funciones.factorial(3) == 6
    assert funciones.factorial(0) == 1
    # assert math.isnan(funciones.factorial(-4)) == True
