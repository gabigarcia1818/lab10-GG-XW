"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    return b/a

def logarithm(a, b): # use math library/raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(b,a)

def exponent(a, b):
    return math.pow(a,b)



