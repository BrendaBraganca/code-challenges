class Solution(object):
    def predictPartyVictory(self, senate):
        fila_r = deque()
        fila_d = deque()
        for i, s in enumerate(senate):
            if(s=='R'):
                fila_r.append(i)
            else:
                fila_d.append(i)
        while fila_r and fila_d:
            ind_r = fila_r.popleft()
            ind_d = fila_d.popleft()
            if(ind_r < ind_d):
                fila_r.append(ind_r + len(senate))
            else:
                fila_d.append(ind_d + len(senate))
        if(fila_r):
            return 'Radiant'
        return 'Dire'