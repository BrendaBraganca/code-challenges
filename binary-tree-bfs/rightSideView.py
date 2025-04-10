class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        fila = deque([root])
        resultado = []
        while fila:
            tam_nivel = len(fila)
            for i in range(tam_nivel):
                no = fila.popleft()
                if(i == tam_nivel - 1):
                    resultado.append(no.val)
                if(no.left):
                    fila.append(no.left)
                if(no.right):
                    fila.append(no.right)
        return resultado