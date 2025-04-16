class Solution(object):
    def maxLevelSum(self, root):
        maior_soma = float('-inf')
        result = 0
        nivel = 0
        fila = collections.deque()
        fila.append(root)
        while(fila):
            nivel+=1
            soma_nivel_atual = 0
            for i in range(len(fila)):
                no_atual = fila.popleft()
                soma_nivel_atual += no_atual.val
                if no_atual.left:
                    fila.append(no_atual.left)
                if no_atual.right:
                    fila.append(no_atual.right)
            if(maior_soma < soma_nivel_atual):
                maior_soma = soma_nivel_atual
                result = nivel
        return result