# 0-1 Knapsack Problem
# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

# Input:
# N = 3
# W = 4
# values[] = {1,2,3}
# weight[] = {4,5,1}

# Output: 3
# Your Task:
# Complete the function knapSack() which takes maximum capacity W, weight array wt[], value array val[] and number of items n as a parameter and returns the maximum possible value you can get.

# Expected Time Complexity: O(N*W).
# Expected Auxiliary Space: O(N*W)

# Constraints:
# 1 ≤ N ≤ 1000
# 1 ≤ W ≤ 1000
# 1 ≤ wt[i] ≤ 1000
# 1 ≤ v[i] ≤ 1000

class Solution:

    def knapsack(self, N, W, values, weights):
        values = [0] + values
        weights = [0] + weights
        dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
        for i in range(1,N+1):
            for j in range(W+1):
                if j-weights[i] >= 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][W]

if __name__ == "__main__":
    N = 3
    W = 4
    values = [1,2,3]
    weights = [4,5,1]
    # N = 4
    # W = 8
    # values = [1,2,5,6]
    # weights = [2,3,4,5]
    s = Solution()
    answer = s.knapsack(N,W,values,weights)
    print(answer)