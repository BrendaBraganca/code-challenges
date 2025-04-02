class Solution(object):
    def countBits(self, n):
        dp = [0] * (n+1)
        up = 1
        for i in range(1,n+1):
            if(up*2 == i):
                up =i
            dp[i] = 1 + dp[i-up]
        return dp