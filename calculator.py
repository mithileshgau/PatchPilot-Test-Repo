def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    # BUG: This should be a * b, but we are returning an addition
    return a + b

def divide(a, b):
    # BUG: Not handling division by zero correctly
    if b == 0:
        return "Cannot divide by zero"
    return a / b
