class Solution(object):
    def findJudge(self, n, trust):
        confiado = [0] * (n +1)
        confia = [0] * (n+1)


        for a, b in trust:
            confia[a]+=1
            confiado[b]+=1
        for i in range(1, n+1):
            if confiado[i] == n-1 and confia[i] == 0:
                return i
        return -1