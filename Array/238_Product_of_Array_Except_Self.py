class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        front_product = nums.copy()
        back_product = nums.copy()
        size = len(nums)
        for i in range(1, size):
            front_product[i] = nums[i]*front_product[i-1]
            back_product[size-1-i] = back_product[size-i] * nums[size-1-i]
        for i in range(size):
            if i == 0:
                nums[i] = back_product[1]
            if i == size - 1:
                nums[i] = front_product[i-1]
            else:
                nums[i] = front_product[i-1]*back_product[i+1]
        return nums


class Solution_best:
    """
    Only use one extra array as output, and go forward and backward to get the results.
    """
    def productExceptSelf(self, nums):
            res = [1] * len(nums)
            p = 1
            for i in range(len(nums)):
                res[i] *= p
                p *= nums[i]

            p = 1
            for i in range(len(nums)-1, -1, -1):
                res[i] *= p
                p *= nums[i]

            return res
