class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = len(nums)/2
        nums.sort()
        cur_num = majority_num = nums[0]
        count = 1
        for num in nums[1:]:
            if num != cur_num:
                if count >= max_count:
                    max_count = count
                    majority_num = cur_num
                    count = 1
                    cur_num = num
                else:
                    cur_num = num
                    count = 1
            else:
                count = count + 1
        if count >= max_count:
            majority_num = nums[len(nums)-1]
        return majority_num


class ElegantSolution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The smart part is divide length by float 2.0, not 2
        majority_count = len(nums)/2.
        temp = []
        for num in nums:
            if num not in temp:
                temp.append(num)
                # Use list.count()
                if nums.count(num) >= majority_count:
                    return num
                    break
