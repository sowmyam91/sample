def factorial(n):
    if n == 1:
        return 1
    else:
        yield n * factorial(n-1)
