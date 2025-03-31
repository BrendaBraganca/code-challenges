class Solution(object):
    def isValid(self, s):
        pilha = []
        for c in s:
            if(c != '}' and c != ']' and c != ')'):
                pilha.append(c)
            else:
                if(c == '}' and pilha[-1] == '{'):
                    pilha.pop()
                elif(c == ')' and pilha[-1] == '('):   
                    pilha.pop()
                elif(c == ']' and pilha[-1] == '['):
                    pilha.pop()
                else:
                    return False
        if(len(pilha) == 0):
            return True
        return False  