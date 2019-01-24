class Solution:
    """
    Find the Kth largest element in a unsorted array
    1. Select Sort. According to the K value, we can try ascending sort or descending sort.
       The tricky thing is the different k value setting for ascending or descending
    2.
    """
    def selectSortAscend(self, nums, k):
        for i in range(k):
            min_index = i
            min_val = nums[i]
            for j in range(i, len(nums)):
                if nums[j] < min_val:
                    min_val = nums[j]
                    min_index = j
            nums[min_index] = nums[i]
            nums[i] = min_val
        return nums[k-1]

    def selectSortDescend(self,nums,k):
        for i in range(k):
            max_index = i
            max_val = nums[i]
            for j in range(i, len(nums)):
                if nums[j] > max_val:
                    max_val = nums[j]
                    max_index = j
            nums[max_index] = nums[i]
            nums[i] = max_val
        return nums[k-1]


    def findKthLargestSelectedSort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_len = len(nums)
        if k < nums_len/2:
            return self.selectSortDescend(nums,k)
        else:
            return self.selectSortAscend(nums, nums_len - k + 1)


    def findKthLargestHeap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]
