import math
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a*b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm: base must be > 0 and ≠ 1, and argument must be > 0.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm arguments must be positive.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    if a<0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)
