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
print(so1.isValidSudoku(test_d))
