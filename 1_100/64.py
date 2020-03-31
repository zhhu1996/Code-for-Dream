class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # # 1. 二维动态规划
        # rows, cols = len(grid), len(grid[0])
        # dp = [[0]*cols for i in range(rows)]
        # dp[0][0] = grid[0][0]
        # for i in range(1, rows):
        #     dp[i][0] = dp[i-1][0] + grid[i][0]
        # for j in range(1, cols):
        #     dp[0][j] = dp[0][j-1] + grid[0][j]
        # for i in range(1, rows):
        #     for j in range(1, cols):
        #         dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # return dp[rows-1][cols-1]

        # 2. 一维动态规划
        rows, cols = len(grid), len(grid[0])
        dp = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if j == 0:
                    dp[j] = dp[j] + grid[i][j]
                elif i == 0:
                    dp[j] = dp[j-1] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]
