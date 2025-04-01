class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            pts = questions[i][0]
            pula = questions[i][1]
            prox = i + pula + 1
            dp[i] = max(pts + (dp[prox] if prox < n else 0), dp[i + 1])
        
        return dp[0]
    