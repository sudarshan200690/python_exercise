import sys

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f
result = fact(5)
print(result)

# Factorial via recursion:
sys.getrecursionlimit()
sys.setrecursionlimit(1500)
def factorial(p):
    if (p == 0):
        return 1
    fact = p * factorial(p-1)
    return fact
res = factorial(2)
print(res)
