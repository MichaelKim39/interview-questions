import math
# INPUT: 32 Bit signed integer
# OUTPUT: Integer with digits reversed
# INFO: 32-bit signed integer range: [−2^31,  2^31 − 1].


def getDigitN(num, n):
    return num // 10**n % 10


def getNumDigits(num):
    digits = 0
    if num > 0:
        return int(math.log10(num)) + 1
    elif num == 0:
        return 1
    else:
        return int(math.log10(-num)) + 2


class Solution:
    # def reverse(self, x: int) -> int:
    #     if x == 0:
    #         return 0
    #     num = str(abs(x))
    #     while num[-1] == '0':
    #         num = num[:-1]
    #     stack = []
    #     res = ""
    #     for i in range(len(num)):
    #         stack.append(num[i])
    #     for i in range(len(num)):
    #         res += stack.pop()
    #     if x > 0:
    #         return int(res)
    #     elif x < 0:
    #         return -int(res)

    # def reverse(self, x: int) -> int:
    #     if x == 0:
    #         return 0
    #     sign = (x > 0) - (x < 0)
    #     reverse = int(str(sign * x)[::-1])
    #     return reverse

    # def reverse(self, x: int) -> int:
    #     num = str(x)
    #     if x < 0:
    #         x = int(num[0] + num[1:][::-1])
    #     if x == 0:
    #         return 1
    #     if x > 0:
    #         x = int(num[::-1])
    #     return x if -2147483648 <= x <= 2147483647 else 0

    def reverse(self, x: int) -> int:
        sign = (x > 0) - (x < 0)
        # Force positive, cast from reversed string back to int
        # Int casting reversed string removes prepending zeroes
        rev = int(str(x * sign)[::-1])
        # Add back sign and check range
        return sign * rev if (-2 ** 31 <= x <= ((2 ** 31) - 1)) else 0


def main():
    solution = Solution()
    print(solution.reverse(2100))


if __name__ == "__main__":
    main()
