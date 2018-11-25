# Solution from https://leetcode.com/problems/maximum-product-subarray/discuss/48243/In-Python-can-it-be-more-conciseself. Concise and beautiful.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = small = big = nums[0]
        for n in nums[1:]:
            big, small = max(n, n*big, n*small), min(n, n*big, n*small)
            maximum = max(maximum, big)
        return maximum
