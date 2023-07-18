class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ['' for _ in range(numRows)]
        row_index = 0
        for ch in s:
            rows[row_index] += ch
            if row_index < numRows - 1:
                row_index += 1
            elif row_index > 0:
                row_index -= 1
        return ''.join(rows)
