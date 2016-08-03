# encoding: utf-8

"""
     Ercan Can
     Program icin gerekli olan benchmark fonksiyonlarini icerir
"""
__author__ = "ercanc"

# imports

import math

# functions

def fitness_rosenbrock(x):
    val = 0
    for i in range(len(x) - 1):
        val += 100 * ((x[i] ** 2) - x[i + 1]) ** 2 + (1 - x[i]) ** 2
    return val

def fitness_schwefel(x):
    alpha = 1.2
    val = 0
    for i in range(len(x)):
        val += x[i] * math.sin(math.sqrt(math.fabs(x[i])))
    return float(val) + alpha * len(x)

def fitness_rastrigin(x):
    val = 10 * len(x)
    for i in range(len(x)):
        val += x[i] ** 2 - (10 * math.cos(2 * math.pi * x[i]))
    return val