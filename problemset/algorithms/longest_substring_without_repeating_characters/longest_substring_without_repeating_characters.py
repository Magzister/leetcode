class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        char = set()

        while r < len(s):
            if s[r] not in char:
                char.add(s[r])
                r += 1
            else:
                longest = max(r - l, longest)
                if s[l] == s[r]:
                    l += 1
                else:
                    while s[l] != s[r] and l < r:
                        char.remove(s[l])
                        l += 1
                    if l < r:
                        l += 1
                r += 1
        longest = max(r - l, longest)

        return longest
