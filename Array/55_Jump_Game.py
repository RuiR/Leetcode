class Solution:
    """

    Space complexity: O(1)
    Time complexity: O(N-1)
    """

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = len(nums)-1
        i = len(nums) -2
        while i >= 0:
            if i + nums[i] >= last:
                last = i
            i = i - 1
        return (last == 0)



class Solution:
    """
    Time exceed
    Time complexity: O(N(0)*N(1)*N(2)***N(N-2)), may not be that large with pruning, but still quite quite complex

    """

    def partJump(self, index, nums):
        if index == len(nums) - 1:
            return True
        elif index > len(nums) - 1:
            return False
        else:
            i = nums[index]
            if i == 0:
                return False
            while i >= 1:
                if self.partJump(index + i, nums):
                    return True
                else:
                    i = i - 1
            return False

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.partJump(0, nums)


class Solution:
    """
    Time exceed when the value in array is very large although using previous saved information
    Space complexity: O(N)
    Time complexity: 最多是O(N*N)
    """
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_nums = len(nums)
        jump_to_end = []
        for i in range(len_nums):
            jump_to_end.append(False)
        jump_to_end[-1] = True
        j = len_nums - 2
        while j >= 0:
            if nums[j] == 0:
                jump_to_end[j] = False
            else:
                for step in range(1, nums[j] + 1):
                    if jump_to_end[j + step]:
                        jump_to_end[j] = True
                        break
            j = j - 1
        return jump_to_end[0]
