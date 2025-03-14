class Solution(object):
    def maxVowels(self, s, k):
        somaJanela = 0
        maxVow = 0
        lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        def eVogal(a):
            if a in lst:
                return True
            return False
        
        for i in range(k):
            if s[i] in lst:
                somaJanela+=1
        maxVow = somaJanela
        for i in range(k, len(s)):
            if s[i] in lst:
                somaJanela+=1
            if s[i - k] in lst:
                somaJanela-=1
            maxVow = max(maxVow, somaJanela)
        return maxVow
        