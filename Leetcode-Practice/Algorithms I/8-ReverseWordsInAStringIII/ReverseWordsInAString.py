class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        for i in range(len(s)):
            s[i] = list(s[i])
            l, r = 0, len(s[i])-1
            while (l < r):
                s[i][l], s[i][r] = s[i][r], s[i][l]
                l += 1
                r -= 1
            s[i] = ''.join(s[i])
        s = ' '.join(s)
        return s
            