class Solution(object):
    def uniqueOccurrences(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        contagens = set()
        for cont in freq.values():
            if cont in contagens:
                return False
            contagens.add(cont)
        return True      