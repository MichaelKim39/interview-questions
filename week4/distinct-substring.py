# INPUT: String of alphabetic characters
# OUTPUT: Lenghth of longest substring without repeating characters
# INFO:
# EXAMPLE: abcabcbb - abc length 3

class Solution:

    # NOTE: Attempt 1
    # Use fact that substrings are contiguous
    # Gradually add characters from string into consideration
    # Once conflict found, remove characters upto conflict point
    # Maintain max substring length variable
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        readChars = dict()  # (char: bool)
        for i in range(len(s)):
            if s[i] in readChars:
                s = s[i:]
            else:
                readChars[s[i]] = True

    # NOTE: Solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        window_start = 0
        mapping = dict()  # (character: latestOccurenceIndex)

        for window_end in range(len(s)):
            if s[window_end] in mapping:
                window_start = max(window_start, mapping[s[window_end]] + 1)
            mapping[s[window_end]] = window_end
            max_length = max(max_length, window_end - window_start + 1)
        return max_length
