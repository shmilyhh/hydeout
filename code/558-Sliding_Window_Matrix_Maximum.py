import sys
class Solution:
    # @param {int[][]} matrix an integer array of n * m matrix
    # @param {int} k an integer
    # @return {int} the maximum number
    def maxSlidingWindow2(self, matrix, k):
        # Write your code here
        rows = len(matrix)
        cols = len(matrix[0])
        
        sums = [[0 for j in range(cols+1)] for i in range(rows+1)]

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                sums[i][j] = matrix[i-1][j-1] + sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1]
        
        maximum = -sys.maxsize - 1
        for i in range(k, rows+1):
            for j in range(k, cols+1):
                s = sums[i][j] - sums[i][j-k] - sums[i-k][j] + sums[i-k][j-k]
                
                if s < maximum:
                    maximum = s
        return s