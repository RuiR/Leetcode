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

class Solution1:
    def isValidSudoku(self, board):
        rows = [[] for _ in range(0, 9)]
        cols = [[] for _ in range(0, 9)]
        areas = [[] for _ in range(0, 9)]
        for i in range(0,9):
            for j in range(0,9):
                entry = board[i][j]
                if entry == ".":
                    continue
                area_id = i // 3 * 3 + j // 3
                if entry in rows[i] or entry in cols[j] or entry in areas[area_id]:
                    return False
                else:
                    rows[i].append(entry)
                    cols[j].append(entry)
                    areas[area_id].append(entry)
        return True
so1 = Solution1()