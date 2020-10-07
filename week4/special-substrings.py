# INPUT: A string
# OUTPUT: Number of special substrings
# INFO: Special substring = all same character || all but middle same character

def substrCount(n, s):
    special_count = 0

    for window_size in range(1, n+1):
        window_start = 0
        window_end = 0 + window_size
        while window_end <= n:
            if isSpecial(s[window_start:window_end]):
                special_count += 1
            window_start += 1
            window_end += 1

    def isSpecial(substring):
        allSame = True
        allSameButMiddle = True
        length = len(substring)

        def checkAllSame():
            for i in range(length-1):
                if substring[i] != substring[i+1]:
                    return False
            return True

        if checkAllSame():
            allSame = True
        elif length % 2 == 1:
            middleIndex = (length // 2) + 1
            substring.remove(middleIndex)
            allSameButMiddle = checkAllSame()

        return allSame or allSameButMiddle

    return special_count
