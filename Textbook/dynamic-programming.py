from typing import List


def recursive_fib(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return recursive_fib(num - 1) + recursive_fib(num - 2)


def cache_fib(num: int) -> int:
    fibs = [False] * (num+1)
    return cache_fib_rec(num, fibs)


def cache_fib_rec(num: int, fibs: List[int or bool]) -> int:
    if (num == 0 or num == 1):
        return num

    if fibs[num]:
        return fibs[num]
    return cache_fib_rec(num - 1, fibs) + cache_fib_rec(num - 2, fibs)


def main():
    print("Main")
    print(recursive_fib(10))
    print(cache_fib(10))


if __name__ == "__main__":
    main()
