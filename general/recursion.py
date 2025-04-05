'''
def factorial(n):
    # base case, when n = 0, stops making calls and returns 1
    if n == 0:
        return 1
    # calls itself, waits for the result to multiply by calling param so goes on stack
    return n * factorial(n-1)

print(factorial(5))

def fibonacci(n):
    print(f"Entering fibonacci({n})")
    if n == 0 or n == 1:
        print(f"Base case reached with fibonacci({n}) = {n}")
        return n
    result = fibonacci(n - 1) + fibonacci(n - 2)
    print(f"Returning from fibonacci({n}) with result = {result}")
    return result

def fib_memo(n, memo=None):
    print(f"Entering fibonacci({n})")
    if memo == None:
        memo = {}
    if n in memo:
        print(f"{n} found in memo")
        return memo[n]
    
    if n == 0 or n == 1:
        print(f"base case for {n}")
        memo[n] = n
        return n
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    print(f"Returning from fibonacci({n}) with result = {memo[n]}")
    return memo[n]
    

print(fib_memo(5))

'''

def fact_tail(n, accumulator=1):
    print(f"Entering fact_tail({n})")
    if n == 0:
        print(f"base case accumulator = {accumulator}")
        return accumulator
    
    accumulator = accumulator * n
    print(f"recusring fact_tail({n-1}) accumulator = {accumulator}")
    return fact_tail(n - 1, accumulator)
    
print(fact_tail(5))