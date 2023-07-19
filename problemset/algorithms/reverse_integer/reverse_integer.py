class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x > 0:
            x, mod = divmod(x, 10)
            result *= 10
            result += mod
        return result * sign if result < 2147483647 else 0
