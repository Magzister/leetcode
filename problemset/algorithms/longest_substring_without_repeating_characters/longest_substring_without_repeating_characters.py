class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 1 if len(s) else 0
        letters_set = {s[0]} if len(s) else set()
        i = j = 0
        while i < len(s) - 1:
            if j < len(s) - 1:
                if s[j + 1] not in letters_set:
                    j += 1
                    letters_set.add(s[j])
                    if len(letters_set) > result:
                        result = len(letters_set)
                else:
                    letters_set.remove(s[i])
                    i += 1
            else:
                letters_set.remove(s[i])
                i += 1
        return result
