"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return node
        fila = deque([node])
        clones = {node.val: Node(node.val, [])}
        while fila:
            atual = fila.popleft()
            clone_atual = clones[atual.val]
            for vizinho in atual.neighbors:
                if vizinho.val not in clones:
                    clones[vizinho.val] = Node(vizinho.val, [])
                    fila.append(vizinho)
                clone_atual.neighbors.append(clones[vizinho.val])
        return clones[node.val]