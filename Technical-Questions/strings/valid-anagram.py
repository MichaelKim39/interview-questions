class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = dict()
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        for char in t:
            if char in char_freq:
                char_freq[char] -= 1
            else:
                return False

        for value in char_freq.values():
            if value != 0:
                return False

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26
        for char in s:
            arr1[ord(char) - ord('a')] += 1
        for char in t:
            arr2[ord(char) - ord('a')] += 1
        return arr1 == arr2
