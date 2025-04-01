class Solution(object):
    def longestValidParentheses(self, s):
        pilha = [-1]
        maxAcc = 0
        for i,c in enumerate(s):
            if(c == '('):
                pilha.append(i)
            else:
                pilha.pop()
                if(pilha):
                    maxAcc = max(maxAcc, i - pilha[-1])
                else:
                    pilha.append(i)
        return maxAcc