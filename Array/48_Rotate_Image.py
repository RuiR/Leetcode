#

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # range(0,n//2) can be written as range(n//2)
        for p in range(0, n//2):
            if p > n - p:
                break
            else:
                for q in range(p, n - p - 1):
                    # The following value transfer can be done in one sentence like
                    # A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         # A[~j][i], A[~i][~j], A[j][~i], A[i][j]
                    tmp = matrix[p][q]
                    matrix[p][q] = matrix[abs(n-1-q)][p]
                    matrix[abs(n-1-q)][p] = matrix[abs(n -1- p)][abs(n - 1 - q)]
                    matrix[abs(n - 1 -p)][abs(n - 1 - q)] = matrix[q][abs(n -1 - p)]
                    matrix[q][abs(n - 1 - p)] = tmp

class SmartSolution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
