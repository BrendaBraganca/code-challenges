class Solution(object):
    def pivotIndex(self, nums):
        somaEsq = 0
        somaDir = sum(nums)
        for i, elemento in enumerate(nums):
            somaDir -= elemento
            if somaEsq == somaDir:
                return i      
            somaEsq += elemento
        return -1