class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        grafo = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            grafo[b].append(a)
        preto = set()
        cinza = set()

        def dfs(v):
            preto.add(v)
            cinza.add(v)
            for vizinho in grafo[v]:
                if vizinho not in preto: #se o nó é branco
                    if dfs(vizinho):
                        return True
                elif(vizinho in cinza):
                    return True
            cinza.remove(v)
            return False
        
        for v in range(numCourses):
            if v not in preto:
                if dfs(v):
                    return False #esta em ciclo 
        return True #nao tem ciclo