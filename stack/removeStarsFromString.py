class Solution(object):
    def removeStars(self, s):
        pilha = []
        for letra in s:
            if letra == '*':
                pilha.pop() 
            else:
                pilha .append(letra)  
        return ''.join(pilha)