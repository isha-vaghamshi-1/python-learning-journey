# WAF to find the factorial of n. (n is the parameter

def factorial(n):
    print(n)
    if n == 0:
        return 1
    else:    
        return n * factorial(n-1)

print(factorial(5))