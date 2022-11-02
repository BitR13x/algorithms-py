def fib(n, memo):
    """Fibonacci sequence, recursion solution with memoize O(n)"""
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
    memo[n] = result
    return result

def fib_bottom_up(n):
    """Fibonacci sequence, bottom up solution which creates a list and filling the list until n is reached O(n)"""
    if n == 1 or n == 2:
        return 1

    bottom_up = [1, 1]
    for i in range(3, n):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]

    return bottom_up[i]