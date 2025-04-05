
def print_f(n):
    if n == 0:
        return
    print(n)
    print_f(n - 1)
    
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print_f(5)
print(factorial(5))