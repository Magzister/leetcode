from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        total = len(nums1) + len(nums2)
        half = total // 2

        while l <= r + 1:
            partition_nums1 = (l + r) // 2
            partition_nums2 = half - partition_nums1 - 2

            max_left_nums1 = nums1[partition_nums1] if partition_nums1 >= 0 else float('-inf')
            min_right_nums1 = nums1[partition_nums1 + 1] if partition_nums1 < len(nums1) - 1 else float('inf')
            max_left_nums2 = nums2[partition_nums2] if partition_nums2 >= 0 else float('-inf')
            min_right_nums2 = nums2[partition_nums2 + 1] if partition_nums2 < len(nums2) - 1 else float('inf')

            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if total % 2 != 0:
                    return min(min_right_nums1, min_right_nums2)
                else:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
            else:
                if max_left_nums1 <= min_right_nums2:
                    l = partition_nums1 + 1
                else:
                    r = partition_nums1 - 1

        raise ValueError("Input arrays are not sorted properly.")
