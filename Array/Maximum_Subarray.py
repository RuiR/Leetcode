class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = cur_sum = nums[0]
        i = 0
        for i in range(1, len(nums)):
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum + nums[i] > nums[i]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]

        return max(max_sum, cur_sum)

    def maxSubarray_Elegant(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
