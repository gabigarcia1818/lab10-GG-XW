"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/gabigarcia1818/lab10-GG-XW.git
# Partner 1: Gabrielle Garcia
# Partner 2: Wanchang Xiong

# First example
import math

def mul(a,b):
    return a * b
def div(a, b):
    if a==0:
        raise ZeroDivisionError
    return b/a

def exp(a, b):
    return math.pow(a, b)

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def logarithm(a, b): # use math library/raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(b,a)

