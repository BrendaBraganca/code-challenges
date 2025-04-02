class Solution(object):
    def fib(self, n):
        if(n == 1 or n == 0):
            return n
        dp = [0, 1]
        for i in range(2, n+1):
            dp.append(dp[i-2] + dp[i-1])
        return dp[-1]