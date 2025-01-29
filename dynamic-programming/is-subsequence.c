bool isSubsequence(char* s, char* t) {
    int m = strlen(s);
    int n = strlen(t);
    
    if (m == 0) return true;
    
    int dp[m + 1][n + 1];

    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            } else if (s[i - 1] == t[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = dp[i][j - 1];
            }
        }
    }
    
    return dp[m][n] == m;
}