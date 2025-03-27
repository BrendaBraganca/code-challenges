class Solution(object):
    def equalPairs(self, grid):
        acc_linha = Counter(tuple(linha) for linha in grid)

        acc = 0
        for col in zip(*grid):
            acc += acc_linha[col]

        return acc
        