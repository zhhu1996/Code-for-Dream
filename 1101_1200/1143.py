class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 经典动态规划题目：LCS
        # dp[i][j] = dp[i-1][j-1] + 1, if s1[i] = s2[j]
        # dp[i][j] = max(dp[i-1][j], dp[i][j-1]), else
        n1, n2 = len(text1), len(text2)
        dp = [[0]*(n2+1) for i in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n1][n2]