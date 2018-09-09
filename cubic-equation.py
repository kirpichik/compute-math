#!/usr/bin/env python3
# coding: utf-8

################################################################################
# Данный модуль добавляет функцию вычисления корней кубического уравнения вида:
# f(x) = x ^ 3 + a * x ^ 2 + b * x + c
################################################################################

from custom_math import find_interval_root
from custom_math import discriminant
from custom_math import find_quadratic_equation_roots
from custom_math import inf


# Вычисляет корни кубического уравнения вида:
# f(x) = x ^ 3 + a * x ^ 2 + b * x + c
def find_cubic_equation_roots(eps, delta, a, b, c):

    # Подсчитывает значение функции в точке
    def calc_value(x):
        return x ** 3 + a * x ** 2 + b * x + c


    # Случай D >= eps ^ 2
    def positive_discriminant():
        alpha, beta = sorted(find_quadratic_equation_roots(eps, 3, 2 * a, b))
        fun_alpha = calc_value(alpha)
        fun_beta = calc_value(beta)

        if fun_alpha > eps and fun_beta > eps:
            return (find_interval_root(eps, delta, inf, alpha, calc_value),)
        elif fun_alpha < -eps and fun_beta < -eps:
            return (find_interval_root(eps, delta, beta, inf, calc_value),)
        elif fun_alpha > eps and abs(fun_beta) < eps:
            return (beta, find_interval_root(eps, delta, inf, alpha, calc_value))
        elif abs(fun_alpha) < eps and fun_beta < -eps:
            return (alpha, find_interval_root(eps, delta, beta, inf, calc_value))
        elif fun_alpha > eps and fun_beta < -eps:
            first = find_interval_root(eps, delta, inf, alpha, calc_value)
            second = find_interval_root(eps, delta, alpha, beta, calc_value)
            third = find_interval_root(eps, delta, beta, inf, calc_value)
            return (first, second, third)
        elif abs(fun_alpha) < eps and abs(fun_beta) < eps:
            return ((alpha + beta) / 2,)


    # Случай D < eps ^ 2
    def negative_discriminant():
        value = calc_value(0) # f(0) = c

        if abs(value) < eps:
            return (0,)
        elif value < -eps:
            return (find_interval_root(eps, delta, 0, inf, calc_value),)
        elif value > eps:
            return (find_interval_root(eps, delta, inf, 0, calc_value),)


    # Дискриминант производной
    D = discriminant(3, 2 * a, b)
    if D < eps ** 2:
        return negative_discriminant()
    else:
        return positive_discriminant()


def main():
    import sys

    if len(sys.argv) != 6:
        print("Required args: eps, delta, a, b, c")
        return

    eps, delta, a, b, c = [float(arg) for arg in sys.argv[1:]]
    print(find_cubic_equation_roots(eps, delta, a, b, c))


if __name__ == "__main__":
    main()

