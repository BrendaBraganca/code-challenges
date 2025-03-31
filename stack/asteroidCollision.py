class Solution(object):
    def asteroidCollision(self, asteroids):
        pilha = []
        for ast in asteroids:
            while pilha and ast<0 and pilha[-1] >0:
                ult = pilha.pop()
                if(abs(ult) > abs(ast)):
                    pilha.append(ult)
                    break
                elif(abs(ult) == abs(ast)):
                    break
            else:
                pilha.append(ast)
        return pilha