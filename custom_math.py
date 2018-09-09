#!/usr/bin/env python3
# coding: utf-8

########################################################
# Данный модуль объединяет различные полезные функции,
# которые могут быть переиспользованы в других модулях.
########################################################

from math import sqrt
from math import inf

#inf = float("inf")

# Ищем корень функции в случае если мы знаем, что он находится
# на интервале [a, b]. Валидным значением для границ интервала
# может быть бесконечность.
# Шагом поиска является delta, а функцию задает параметр func.
def find_interval_root(eps, delta, a, b, func):

    # Подсчитывает вторую границу для приведения бесконечного
    # интервала к конечному.
    def calc_border(delta, a):
        lower = func(a) < 0
        coeff = 1
        while True:
            point = a + coeff * delta
            value = func(point)
            if (lower and value > 0) or (not lower and value < 0):
                return point
            coeff += 1

    print("pre", a, b)

    if a == inf and b == inf:
        raise RuntimeError("Interval is infinite in both directions!")
    elif a == inf:
        border = calc_border(-delta, b)
        return find_interval_root(eps, delta, border, border + delta, func)
    elif b == inf:
        border = calc_border(delta, a)
        return find_interval_root(eps, delta, border - delta, border, func)

    # Разворачиваем аналогичный случай
    if func(a) > 0 and func(b) < 0:
        c = a
        a = b
        b = c

    while True:
        c = (a + b) / 2
        value = func(c)
        if abs(value) <= eps:
            return c
        elif value > eps:
            b = c
        elif value < -eps:
            a = c


# Вычисляет дискриминант квадратного уравнения вида:
# a * x ^ 2 + b * x + c = 0
def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


# Вычисляет корни квадратного уравнения вида:
# a * x ^ 2 + b * x + c = 0
def find_quadratic_equation_roots(eps, a, b, c):
    D = discriminant(a, b, c)

    peps = eps ** 2
    if D < -peps:
        return ()
    elif abs(D) < peps:
        return (-b / (2 * a),)
    elif D >= peps:
        return ((-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a))


if __name__ == "__main__":
    print("This module has no executable part.")

