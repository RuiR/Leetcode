import numpy as np
import collections


class Solution:

    def isValidPart(self, part_arr):
        count_array = collections.Counter(part_arr)
        if sum(count_array.values()) - count_array['.'] > len(count_array.values())-1:
            return False
        else:
            return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        board_arr = np.array(board)
        i = 0
        while i < 9:
            if not self.isValidPart(board_arr[i,:]):
                return False
            if not self.isValidPart(board_arr[:,i]):
                return False
            i += 1

        for row in range(0, 8, 3):
            for col in range(0, 8, 3):
                part_arr = board_arr[row:row+3, col:col+3].ravel()
                if not self.isValidPart(part_arr):
                    return False

        return True

# so = Solution()
# print(so.isValidSudoku(test_d))
