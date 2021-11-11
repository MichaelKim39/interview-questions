# Q: Given a string s, find the longest palindromic substring in s.
# INPUT: String s
# OUTPUT: Longest substring that is a palindrome (spelt same forward as backward)
# INFO: You may assume that the maximum length of s is 1000.


class Solution:
    def longestPalindrome2(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            left_odd = i
            right_odd = i
            left_even = i
            right_even = i + 1
            while (True):
                check_odd = (left_odd >= 0) and (right_odd < len(s))
                check_even = (left_even >= 0) and (right_even < len(s))
                # Break if necessary
                if not check_odd or not check_even:
                    break
                # For palindromes of odd length
                if check_odd and (s[left_odd] == s[right_odd]):
                    substring = s[left_odd:right_odd+1]
                    if len(substring) >= len(longest):
                        longest = substring
                    left_odd -= 1
                    right_odd += 1
                # For palindromes of even length
                if check_even and s[left_even] == s[right_even]:
                    substring = s[left_even:right_even+1]
                    if len(substring) >= len(longest):
                        longest = substring
                    left_even -= 1
                    right_even += 1

        return longest

# ---------------------------------------------------------------------------- #
#                                OPTIMAL VERSION                               #
# ---------------------------------------------------------------------------- #

    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            substring = self.longestSubstr(s, i, i)
            if len(substring) > len(longest):
                longest = substring
            substring = self.longestSubstr(s, i, i+1)
            if len(substring) > len(longest):
                longest = substring
        return longest

    def longestSubstr(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # NOT s[left:right+1] because last iteration has pushed along one more
        return s[left+1:right]

# ---------------------------------------------------------------------------- #
#                                   VERSION 2                                  #
# ----------------------------------------------------------------------------

    # def longestPalindrome(self, s):
    #     res = ""
    #     for i in range(len(s)):
    #         # odd case, like "aba"
    #         tmp = self.helper(s, i, i)
    #         if len(tmp) > len(res):
    #             res = tmp
    #         # even case, like "abba"
    #         tmp = self.helper(s, i, i+1)
    #         if len(tmp) > len(res):
    #             res = tmp
    #     return res

    # # get the longest palindrome, l, r are the middle indexes
    # # from inner to outer
    # def helper(self, s, l, r):
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         l -= 1
    #         r += 1
    #     return s[l+1:r]


def main():
    a = "babad"
    solution = Solution()
    print(solution.longestPalindrome(a))


if __name__ == "__main__":
    main()
