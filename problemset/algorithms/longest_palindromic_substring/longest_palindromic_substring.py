class Solution:
    def longestPalindrome(self, s: str) -> str:
        new_s = '#'.join('^{}$'.format(s))

        n = len(new_s)
        P = [0] * n
        C = R = 0

        for i in range(1, n - 1):
            if i < R:
                mirror_i = C * 2 - i
                P[i] = min(P[mirror_i], R - i)

            while new_s[i - P[i] - 1] == new_s[i + P[i] + 1]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = i + P[i]

        max_len = max(P)
        center_index = P.index(max_len)

        start = (center_index - max_len) // 2
        end = start + max_len

        return s[start:end]
