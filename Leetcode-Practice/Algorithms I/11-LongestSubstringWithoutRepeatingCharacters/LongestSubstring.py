class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        l = 0
        res = 0
        for i in range(len(s)):
            new_char = s[i]
            while (new_char in substring):
                substring.pop(0)
                l += 1
            substring.append(new_char)
            res = max(res, i - l + 1)
        return res