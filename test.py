def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * factorial_rec(n-1)