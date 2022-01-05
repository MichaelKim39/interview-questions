import math

# Primality check
# Only check upto square root due to complementary factors covering latter half


def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        print(i)
        if num % i == 0:
            return False
    return True


# Generating prime list
# Sieve of Eratosthenes
def eratosthenes(max):
    flags = [True, True] + [True] * (max-2)
    prime = 2
    while prime <= int(math.sqrt(max)):
        removeMultiples(prime, flags)
        prime = nextPrime(prime, flags)
    return flags


def removeMultiples(prime, flags):
    for num in range(prime**2, len(flags)):
        if num % prime == 0:
            flags[num] = False


def nextPrime(prime, flags):
    next = prime + 1
    while (not flags[next] & next < len(flags)):
        next += 1
    return next


def main():
    # print(isPrime(29))
    print(eratosthenes(29))


if __name__ == '__main__':
    main()
