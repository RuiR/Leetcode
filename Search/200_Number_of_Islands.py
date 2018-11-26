# Wrong thought: I think if I traverse the grid from left to right and top to down,
# I don't need to check the left and top of the current grid. That would lead to error
# when the island is getting deeper and wider. Then the left and top may not be visited
# before and will be treated as anther island

class Solution(object):
    def traverseGrid(self, index_x, index_y):
        if 0 <= index_x < len(self.grid) and 0 <= index_y < len(self.grid[0]) and self.grid[index_x][index_y] == '1':
            self.grid[index_x][index_y] = '0'
            self.traverseGrid(index_x, index_y + 1)
            self.traverseGrid(index_x + 1, index_y)
            self.traverseGrid(index_x - 1, index_y)
            self.traverseGrid(index_x, index_y - 1)
        else:
            return

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        island_count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if self.grid[i][j] == '1':
                    island_count += 1
                    self.traverseGrid(i, j)
        return island_count
