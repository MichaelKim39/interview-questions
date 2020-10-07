# INPUT: String and target substring dubbed HAYSTACK and NEEDLE
# OUTPUT: Index of first letter of substring where it occurs in the original string. -1 if it does not occur

class Solution:

    # ---------------------------------------------------------------------------- #
    #                                  BRUTE FORCE                                 #
    # ---------------------------------------------------------------------------- #

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle):
                    return i
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        i = 1
        j = 0
        lps = [-1] + [0]*n

        while i < n:
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                lps[i] = j
            else:
                j = lps[j]
        i = j = 0
        while i < h and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = lps[j]
            return i-j if j == n else -1
