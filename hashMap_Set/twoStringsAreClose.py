class Solution(object):
    def closeStrings(self, word1, word2):
        if(set(word1) != set(word2)):
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        return sorted(freq1.values()) == sorted(freq2.values())