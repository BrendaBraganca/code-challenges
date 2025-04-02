class Solution(object):
    def tribonacci(self, n):
        if(n == 0):
            return 0
        if(n < 3):
            return 1
        dp = [0,1,1]
        for i in range(3, n+1):
            dp.append(dp[i-3] + dp[i-2] + dp[i-1])
        return dp[-1] 