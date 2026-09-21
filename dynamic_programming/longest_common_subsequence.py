"""
Longest Common Subsequence (LCS)
-----------------------------------
Given two strings, find the length of their longest common subsequence
(characters in the same relative order, not necessarily contiguous).

Approach: bottom-up DP. dp[i][j] = LCS length of s1[:i] and s2[:j].
If the last characters match, dp[i][j] = dp[i-1][j-1] + 1; otherwise take the
better of dropping the last char of either string.

Time:  O(m * n)
Space: O(m * n)
"""


def lcs_length(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
