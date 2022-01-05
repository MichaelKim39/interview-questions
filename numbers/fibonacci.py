# q3 find fibonacci numbers with a recursive solution (upto n)
# INPUT: integer N
# OUTPUT: Array of fibonacci nums upto N

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
    fibs = [0, 1]
    for i in range(n):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n]