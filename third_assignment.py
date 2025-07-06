# FIRST TASK = FIND THE FACTORIAL

n = int(input("enter the number:"))
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n -1)
    
result = factorial(n)
print(f"factorial of {n} is:", result)


# SECOND TASK = USE THE MATH MODULE

import math

n = int(input("enter the number:"))

def root(n):
    return math.sqrt(n)

def log(n):
    return math.log(n)

def sin(n):
    return math.sin(n)

result = root(n)
print(f"the root of {n} is", result)

result2 = log(n)
print(f"the log of {n} is", result2)

result3 = sin(n)
print(f"the sin of {n} is", result3)

    
    
