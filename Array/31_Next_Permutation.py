class Solution(object):
    def get_switch_index(self, nums, target_value, end_index):
        index = len(nums) - 1
        while index > end_index:
            if nums[index] > target_value:
                return index
            else:
                index = index - 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 2
        flag = 1
        while n >= 0:
            cur_val = nums[n]
            if cur_val < nums[n + 1]:
                flag = 0
                switch_index = self.get_switch_index(nums, cur_val, n)
                nums[n] = nums[switch_index]
                nums[switch_index] = cur_val
                start_index = n + 1
                end_index = len(nums) - 1
                while start_index <= end_index:
                    tmp = nums[start_index]
                    nums[start_index] = nums[end_index]
                    nums[end_index] = tmp
                    start_index = start_index + 1
                    end_index = end_index - 1
                break
            else:
                n = n - 1
                continue
        if flag:
            nums.sort()
